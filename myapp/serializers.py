# myapp/serializers.py
from rest_framework import serializers
from .models import Appointment ,Doctor, Review



class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields="__all__"
        




class DoctorSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields=['id','doctor', 'doctor_name','date_time','problems','status']   
    def get_doctor_name(self, obj):
        return obj.doctor.name      

class ReviewSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()


    class Meta:
        model = Review
        fields = ['id', 'doctor', 'doctor_name',  'review_comment', 'rate']

    def get_doctor_name(self, obj):
        return obj.doctor.name        
        