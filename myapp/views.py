from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Patient
from .serializers import CustomUserSerializer, PatientSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
# Create your views here.
