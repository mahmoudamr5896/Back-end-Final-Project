# myapp/serializers.py
from rest_framework import serializers
from .models import Appointment ,Doctor, Review
from .models import CustomUser, Patient


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
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'doctor_name', 'patient', 'patient_name', 'date_time', 'problems', 'status','Reasone_reject']

    def get_doctor_name(self, obj):
        return obj.doctor.name if obj.doctor else None

    def get_patient_name(self, obj):
        return obj.patient.name if obj.patient else None   


class ReviewSerializer(serializers.ModelSerializer):
    Doctor_Name = serializers.SerializerMethodField()
    User_Name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'Doctor_id', 'Doctor_Name', 'User_id', 'User_Name', 'Review', 'Rate']

    def get_Doctor_Name(self, obj):
        return obj.Doctor_id.name if obj.Doctor_id else None

    def get_User_Name(self, obj):
        return obj.User_id.name if obj.User_id else None





class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
from .models import Availability

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

  