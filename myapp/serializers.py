# myapp/serializers.py
from rest_framework import serializers
<<<<<<< HEAD
from .models import Appointment ,Doctor
=======
from .models import Appointment, Review
>>>>>>> Nardeen

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
<<<<<<< HEAD
        fields="__all__"


class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        Model= Doctor
        fields="__all__"
        
        
=======
        fields = ['id', 'date_time', 'problems', 'status'] 


class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields="__all__"    
>>>>>>> Nardeen
