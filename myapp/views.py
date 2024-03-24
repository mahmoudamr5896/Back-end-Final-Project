from django.http import Http404, HttpResponse , JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from .models import Appointment ,Doctor, Review
from .serializers import AppointmentSerializer ,DoctorsSerializer, ReviewSerializer
from rest_framework import viewsets
from django.core.mail import EmailMultiAlternatives
from .models import Appointment ,Doctor, Payment, Review
from .serializers import AppointmentSerializer ,DoctorsSerializer, PaymentSerializer, ReviewSerializer
from rest_framework import viewsets
import paypalrestsdk
import json


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer
    def get_queryset(self):
        queryset = Doctor.objects.all()
        name_query = self.request.query_params.get('name', None)
        if name_query:
            queryset = queryset.filter(name__icontains=name_query)
        return queryset
    def create(self, request, *args, **kwargs):
        username=request.data["username"]
        name=request.data["name"]
        age=request.data["age"]
        image=request.data["image"]
        experience=request.data["experience"]
        gender=request.data["gender"]
        phone=request.data["phone"]
        location =request.data["location"]
        Doctor.objects.create(username=username,name=name,age=age,image=image,experience=experience,gender=gender,phone=phone,location=location)
        return Response(status=status.HTTP_200_OK)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        respone= super().update(request, *args, **kwargs)
        status = request.data["status"]
        user = User.objects.filter(username__iexact=instance.username).first()
        email  = user.email
        self.send_approve_mail(status,email)
        return respone
    
    @staticmethod
    def send_approve_mail(approve,email):
        if approve:
            message = "Your appointment has been approved , visit your profile for more informations."
            email_subject = "appointment approved"
        else:
            message = "Your appointment has been rejected , visit your profile for more informations."
            email_subject = "appointment rejected"

        try:
          
            email_sender = "sender@example.com"
            email_recipient = email

            email_message = EmailMultiAlternatives(
                subject=email_subject,
                body=message,
                from_email=email_sender,
                to=[email_recipient, ]
            )
            email_message.send(fail_silently=False)
        except Exception as e:
            print(e)
class ReviewFunBaseView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()

        # Get the 'doctor_id' from the query parameters if provided
        doctor_id = self.request.query_params.get('doctor_id')

        if doctor_id:
            queryset = queryset.filter(Doctor_id=doctor_id)

        return queryset

from .models import CustomUser, Patient
from .serializers import CustomUserSerializer, PatientSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    def create(self, request, *args, **kwargs):
        username=request.data["username"]

        name=request.data["name"]
        age=request.data["age"]
        image=request.data["image"]
        weight=request.data["weight"]
        gender=request.data["gender"]
        phone=request.data["phone"]
        height =request.data["height"]
        medical_history=request.data["medical_history"]
        Patient.objects.create(username=username,name=name,age=age,image=image,weight=weight,gender=gender,phone=phone,height=height, medical_history= medical_history)
        return Response(status=status.HTTP_200_OK)
    

# views.py
from rest_framework import generics
from .models import Availability
from .serializers import AvailabilitySerializer

from .models import Availability
from .serializers import AvailabilitySerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
     
                 # Get the 'doctor_id' from the query parameters if provided
    def get_queryset(self):
        queryset = Availability.objects.all()
        # Get the 'doctor_id' from the query parameters if provided
        doctor_id = self.request.query_params.get('doctor')

        if doctor_id:
            queryset = queryset.filter(doctor=doctor_id)

        return queryset
 



class DoctorAvailabilityView(APIView):
    def get(self, request, doctor_id):
        try:
            doctor = Doctor.objects.get(pk=doctor_id)
            availability = doctor.generate_availability()  # Assuming you have implemented this method in the Doctor model
            serializer = AvailabilitySerializer(availability)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=404)
        
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


paypalrestsdk.configure({
    "mode": "sandbox", # Use "live" for production
    "client_id": "<YOUR_CLIENT_ID>",
    "client_secret": "<YOUR_CLIENT_SECRET>"
})

def create_payment(request):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "<YOUR_RETURN_URL>",
            "cancel_url": "<YOUR_CANCEL_URL>"
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Item 1",
                    "sku": "item_1",
                    "price": "10.00",
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": "10.00",
                "currency": "USD"
            },
            "description": "This is a test transaction."
        }]
    })

    if payment.create():
        # Redirect the user to the PayPal approval URL
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = link.href
                return redirect(redirect_url)
    else:
        # Handle payment creation errors
        return HttpResponse("Error: " + payment.error)    
    

def meal_plan_api(request, weight_status_id):
        weight_status_map = {
            1: "underweight",
            2: "normal",
            3: "overweight",
            4: "obesity"
        }

def meal_plan_api(request, weight_status_id):
    meal_plans = [
      {"id": 1,
      "day1": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread",
    "snack1": "Greek yogurt with honey and mixed nuts (~300 calories)",
    "lunch": "Koshari topped with caramelized onions (~600 calories)",
    "snack2": "Fresh fruit salad with honey (~150 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~750 calories)"
  },
  "day2": {
    "breakfast": "Shakshuka with sautéed vegetables and whole wheat bread (~400 calories)",
    "snack1": "Cottage cheese with pineapple chunks (~250 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~400 calories)",
    "snack2": "Hummus with raw carrot and cucumber sticks (~200 calories)",
    "dinner": "Stuffed bell peppers with quinoa, black beans, and corn (~750 calories)"
  },
  "day3": {
    "breakfast": "Omelette with spinach, tomatoes, onions, and bell peppers, served with whole wheat toast (~400 calories)",
    "snack1": "Apple slices with almond butter (~200 calories)",
    "lunch": "Egyptian-style chickpea stew with spinach, onions, and garlic, served with whole wheat pita bread (~500 calories)",
    "snack2": "Greek yogurt with berries (~200 calories)",
    "dinner": "Vegetable curry with chickpeas, cauliflower, carrots, and potatoes, served with whole wheat naan bread (~750 calories)"
  },
  "day4": {
    "breakfast": "Egyptian-style scrambled eggs with tomatoes, onions, and bell peppers, served with whole wheat pita bread (~400 calories)",
    "snack1": "Rice cakes with avocado slices and cherry tomatoes (~300 calories)",
    "lunch": "Mujadara topped with caramelized onions and served with tabbouleh salad (~600 calories)",
    "snack2": "Trail mix (nuts and dried fruits) (~250 calories)",
    "dinner": "Vegetable stir-fry with tofu, mushrooms, bok choy, and snow peas, served with quinoa (~750 calories)"
  },
  "day5": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread (~400 calories)",
    "snack1": "Greek yogurt with honey and mixed nuts (~300 calories)",
    "lunch": "Lentil and vegetable curry with spinach, carrots, and zucchini, served with quinoa (~600 calories)",
    "snack2": "Fresh fruit salad with honey (~150 calories)",
    "dinner": "Vegetarian chili with kidney beans, black beans, corn, tomatoes, and bell peppers, served with cornbread (~750 calories)"
  },
  "day6": {
    "breakfast": "Scrambled tofu with tomatoes, onions, spinach, and turmeric, served with whole wheat toast (~400 calories)",
    "snack1": "Carrot and cucumber sticks with hummus (~200 calories)",
    "lunch": "Mixed bean salad with chickpeas, kidney beans, black beans, and lemon-tahini dressing, served with whole wheat pita bread (~600 calories)",
    "snack2": "Low-fat yogurt with berries (~200 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~750 calories)"
  },
  "day7": {
    "breakfast": "Overnight oats with almond milk, chia seeds, bananas, cinnamon, and sliced almonds (~400 calories)",
    "snack1": "Rice cakes with almond butter (~300 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~400 calories)",
    "snack2": "Apple slices with peanut butter (~250 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~750 calories)"
  }},
      {"id": 2,
      "day1": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread (~400 calories)",
    "snack1": "Greek yogurt with honey and mixed nuts (~300 calories)",
    "lunch": "Koshari topped with caramelized onions (~500 calories)",
    "snack2": "Fresh fruit salad with honey (~150 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~650 calories)"
  },
  "day2": {
    "breakfast": "Shakshuka with sautéed vegetables and whole wheat bread (~400 calories)",
    "snack1": "Cottage cheese with pineapple chunks (~250 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~400 calories)",
    "snack2": "Hummus with raw carrot and cucumber sticks (~200 calories)",
    "dinner": "Stuffed bell peppers with quinoa, black beans, and corn (~750 calories)"
  },
  "day3": {
    "breakfast": "Omelette with spinach, tomatoes, onions, and bell peppers, served with whole wheat toast (~400 calories)",
    "snack1": "Apple slices with almond butter (~200 calories)",
    "lunch": "Egyptian-style chickpea stew with spinach, onions, and garlic, served with whole wheat pita bread (~500 calories)",
    "snack2": "Greek yogurt with berries (~200 calories)",
    "dinner": "Vegetable curry with chickpeas, cauliflower, carrots, and potatoes, served with whole wheat naan bread (~750 calories)"
  },
  "day4": {
    "breakfast": "Egyptian-style scrambled eggs with tomatoes, onions, and bell peppers, served with whole wheat pita bread (~400 calories)",
    "snack1": "Rice cakes with avocado slices and cherry tomatoes (~300 calories)",
    "lunch": "Mujadara topped with caramelized onions and served with tabbouleh salad (~600 calories)",
    "snack2": "Trail mix (nuts and dried fruits) (~250 calories)",
    "dinner": "Vegetable stir-fry with tofu, mushrooms, bok choy, and snow peas, served with quinoa (~650 calories)"
  },
  "day5": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread (~400 calories)",
    "snack1": "Greek yogurt with honey and mixed nuts (~300 calories)",
    "lunch": "Lentil and vegetable curry with spinach, carrots, and zucchini, served with quinoa (~600 calories)",
    "snack2": "Fresh fruit salad with honey (~150 calories)",
    "dinner": "Vegetarian chili with kidney beans, black beans, corn, tomatoes, and bell peppers, served with cornbread (~750 calories)"
  },
  "day6": {
    "breakfast": "Scrambled tofu with tomatoes, onions, spinach, and turmeric, served with whole wheat toast (~400 calories)",
    "snack1": "Carrot and cucumber sticks with hummus (~200 calories)",
    "lunch": "Mixed bean salad with chickpeas, kidney beans, black beans, and lemon-tahini dressing, served with whole wheat pita bread (~600 calories)",
    "snack2": "Low-fat yogurt with berries (~200 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~650 calories)"
  },
  "day7": {
    "breakfast": "Overnight oats with almond milk, chia seeds, bananas, cinnamon, and sliced almonds (~400 calories)",
    "snack1": "Rice cakes with almond butter (~300 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~400 calories)",
    "snack2": "Apple slices with peanut butter (~250 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~650 calories)"
  }},
      {"id": 3,
       "day1": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread (~350 calories)",
    "snack1": "Greek yogurt with honey and mixed nuts (~250 calories)",
    "lunch": "Koshari topped with caramelized onions (~400 calories)",
    "snack2": "Fresh fruit salad with honey (~100 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~700 calories)"
  },
  "day2": {
    "breakfast": "Shakshuka with sautéed vegetables and whole wheat bread (~350 calories)",
    "snack1": "Cottage cheese with pineapple chunks (~200 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~350 calories)",
    "snack2": "Hummus with raw carrot and cucumber sticks (~150 calories)",
    "dinner": "Stuffed bell peppers with quinoa, black beans, and corn (~750 calories)"
  },
  "day3": {
    "breakfast": "Omelette with spinach, tomatoes, onions, and bell peppers, served with whole wheat toast (~350 calories)",
    "snack1": "Apple slices with almond butter (~150 calories)",
    "lunch": "Egyptian-style chickpea stew with spinach, onions, and garlic, served with whole wheat pita bread (~400 calories)",
    "snack2": "Greek yogurt with berries (~150 calories)",
    "dinner": "Vegetable curry with chickpeas, cauliflower, carrots, and potatoes, served with whole wheat naan bread (~750 calories)"
  },
  "day4": {
    "breakfast": "Egyptian-style scrambled eggs with tomatoes, onions, and bell peppers, served with whole wheat pita bread (~350 calories)",
    "snack1": "Rice cakes with avocado slices and cherry tomatoes (~200 calories)",
    "lunch": "Mujadara topped with caramelized onions and served with tabbouleh salad (~500 calories)",
    "snack2": "Trail mix (nuts and dried fruits) (~200 calories)",
    "dinner": "Vegetable stir-fry with tofu, mushrooms, bok choy, and snow peas, served with quinoa (~700 calories)"
  },
  "day5": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread (~350 calories)",
    "snack1": "Greek yogurt with honey and mixed nuts (~250 calories)",
    "lunch": "Lentil and vegetable curry with spinach, carrots, and zucchini, served with quinoa (~550 calories)",
    "snack2": "Fresh fruit salad with honey (~100 calories)",
    "dinner": "Vegetarian chili with kidney beans, black beans, corn, tomatoes, and bell peppers, served with cornbread (~750 calories)"
  },
  "day6": {
    "breakfast": "Scrambled tofu with tomatoes, onions, spinach, and turmeric, served with whole wheat toast (~350 calories)",
    "snack1": "Carrot and cucumber sticks with hummus (~150 calories)",
    "lunch": "Mixed bean salad with chickpeas, kidney beans, black beans, and lemon-tahini dressing, served with whole wheat pita bread (~500 calories)",
    "snack2": "Low-fat yogurt with berries (~150 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~700 calories)"
  },
  "day7": {
    "breakfast": "Overnight oats with almond milk, chia seeds, bananas, cinnamon, and sliced almonds (~350 calories)",
    "snack1": "Rice cakes with almond butter (~250 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~350 calories)",
    "snack2": "Apple slices with peanut butter (~200 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~700 calories)"
  }},
      {"id": 4,
      "day1": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread (~300 calories)",
    "snack1": "Greek yogurt with honey and mixed nuts (~200 calories)",
    "lunch": "Koshari topped with caramelized onions (~300 calories)",
    "snack2": "Fresh fruit salad with honey (~100 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~600 calories)"
  },
  "day2": {
    "breakfast": "Shakshuka with sautéed vegetables and whole wheat bread (~300 calories)",
    "snack1": "Cottage cheese with pineapple chunks (~150 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~300 calories)",
    "snack2": "Hummus with raw carrot and cucumber sticks (~100 calories)",
    "dinner": "Stuffed bell peppers with quinoa, black beans, and corn (~650 calories)"
  },
  "day3": {
    "breakfast": "Omelette with spinach, tomatoes, onions, and bell peppers, served with whole wheat toast (~300 calories)",
    "snack1": "Apple slices with almond butter (~100 calories)",
    "lunch": "Egyptian-style chickpea stew with spinach, onions, and garlic, served with whole wheat pita bread (~350 calories)",
    "snack2": "Greek yogurt with berries (~150 calories)",
    "dinner": "Vegetable curry with chickpeas, cauliflower, carrots, and potatoes, served with whole wheat naan bread (~600 calories)"
  },
  "day4": {
    "breakfast": "Egyptian-style scrambled eggs with tomatoes, onions, and bell peppers, served with whole wheat pita bread (~300 calories)",
    "snack1": "Rice cakes with avocado slices and cherry tomatoes (~150 calories)",
    "lunch": "Mujadara topped with caramelized onions and served with tabbouleh salad (~400 calories)",
    "snack2": "Trail mix (nuts and dried fruits) (~150 calories)",
    "dinner": "Vegetable stir-fry with tofu, mushrooms, bok choy, and snow peas, served with quinoa (~600 calories)"
  },
  "day5": {
    "breakfast": "Ful medames with olive oil, tomatoes, onions, and whole wheat pita bread (~300 calories)",
    "snack1": "Greek yogurt with honey and mixed nuts (~200 calories)",
    "lunch": "Lentil and vegetable curry with spinach, carrots, and zucchini, served with quinoa (~450 calories)",
    "snack2": "Fresh fruit salad with honey (~100 calories)",
    "dinner": "Vegetarian chili with kidney beans, black beans, corn, tomatoes, and bell peppers, served with cornbread (~650 calories)"
  },
  "day6": {
    "breakfast": "Scrambled tofu with tomatoes, onions, spinach, and turmeric, served with whole wheat toast (~300 calories)",
    "snack1": "Carrot and cucumber sticks with hummus (~100 calories)",
    "lunch": "Mixed bean salad with chickpeas, kidney beans, black beans, and lemon-tahini dressing, served with whole wheat pita bread (~450 calories)",
    "snack2": "Low-fat yogurt with berries (~150 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~600 calories)"
  },
  "day7": {
    "breakfast": "Overnight oats with almond milk, chia seeds, bananas, cinnamon, and sliced almonds (~300 calories)",
    "snack1": "Rice cakes with almond butter (~200 calories)",
    "lunch": "Egyptian-style lentil soup with whole wheat bread (~300 calories)",
    "snack2": "Apple slices with peanut butter (~150 calories)",
    "dinner": "Vegetable stir-fry with tofu, broccoli, bell peppers, and snap peas, served with quinoa (~650 calories)"
  }
    }
    ]

    for meal_plan in meal_plans:
        if meal_plan["id"] == weight_status_id:
            return JsonResponse(meal_plan)

    return JsonResponse({"error": "meal plan not found"}, status=404)


def nutrition_instructions(request, disease_status_id):
        disease_status_map = {
            1: "Diabetes_Mellitus",
            2: "Hypertension",
            3: "Chronic_Kidney_Disease",
            4: "Heart_Disease"
        }
        
def nutrition_instructions(request,disease_status_id):
    instructions = [
        {"id": 1,
            "name":"Diabetes Mellitus",
            "instructions": [
                "Monitor carbohydrate intake: Focus on consuming complex carbohydrates with a low glycemic index.",
                "Choose healthy fats: Opt for unsaturated fats found in nuts, seeds, avocados, and fatty fish.",
                "Control portion sizes: Eat smaller, balanced meals throughout the day.",
                "Limit added sugars: Minimize intake of sugary beverages, desserts, and processed foods.",
                "Monitor sodium intake: Be cautious of high-sodium foods."
            ]},
        {"id": 2,
            "name":"Hypertension",
            "instructions": [
                "Reduce sodium intake: Limit consumption of high-sodium foods like processed foods and salty snacks.",
                "Increase potassium-rich foods: Consume bananas, oranges, spinach, and sweet potatoes.",
                "Maintain a healthy weight: Focus on a balanced diet and regular physical activity.",
                "Monitor caffeine intake: Limit excessive caffeine consumption."
            ]
        },
        {"id": 3,
            "name":"Chronic Kidney Disease",
            "instructions": [
                "Control protein intake: Reduce overall protein consumption.",
                "Monitor phosphorus and potassium: Limit intake of high-phosphorus and potassium-rich foods.",
                "Manage fluid intake: Follow guidelines to prevent fluid buildup.",
                "Limit salt intake: Lower sodium intake to manage blood pressure and fluid retention.",
                "Monitor calcium and vitamin D: Ensure adequate intake for bone health."
            ]
        },
        {"id": 4,
            "name":"Heart Disease",
            "instructions": [
                "Limit saturated and trans fats: Minimize intake of fried foods, processed meats, and baked goods.",
                "Increase fiber intake: Choose fiber-rich foods like whole grains, legumes, fruits, and vegetables.",
                "Control portion sizes: Eat smaller, balanced meals to maintain a healthy weight.",
                "Manage cholesterol levels: Choose lean protein sources."
            ]
        }
    ]


    for instructions in instructions:
            if instructions["id"] == disease_status_id:
                return JsonResponse(instructions)
            
    return JsonResponse({"error": "meal plan not found"}, status=404)