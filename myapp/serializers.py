# myapp/serializers.py
from rest_framework import serializers
from .models import Appointment ,Doctor
from .models import Appointment, Review

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields="__all__"


class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        Model= Doctor
        fields="__all__"
        
        
        fields = ['id', 'date_time', 'problems', 'status'] 


class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields="__all__"    
