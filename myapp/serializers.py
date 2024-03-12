# myapp/serializers.py
from rest_framework import serializers
from .models import Appointment ,Doctor

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields="__all__"


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields="__all__"
        
        
