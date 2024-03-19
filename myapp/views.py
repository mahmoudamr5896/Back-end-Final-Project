from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment ,Doctor, Review
from .serializers import AppointmentSerializer ,DoctorsSerializer, ReviewSerializer
from rest_framework import viewsets

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