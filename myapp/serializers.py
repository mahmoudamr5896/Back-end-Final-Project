from rest_framework import serializers
from rest_framework import serializers
from .models import CustomUser, Patient
from rest_framework import serializers
from .models import Appointment ,Doctor, Review

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields="__all__"

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
        fields = ['id', 'doctor', 'doctor_name', 'patient', 'patient_name', 'date_time', 'problems', 'status']

    def get_doctor_name(self, obj):
        return obj.doctor.name if obj.doctor else None

    def get_patient_name(self, obj):
        return obj.patient.name if obj.patient else None

class ReviewSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'doctor', 'doctor_name', 'patient', 'patient_name', 'review_comment', 'rate']

    def get_doctor_name(self, obj):
        return obj.doctor.name if obj.doctor else None

    def get_patient_name(self, obj):
        return obj.patient.name if obj.patient else None

