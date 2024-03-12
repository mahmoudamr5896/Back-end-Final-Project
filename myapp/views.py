# from django.shortcuts import render

# # Create your views here.
# # views.py
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Appointment
# from .serializers import AppointmentSerializer

# class AppointmentListView(APIView):
#     def get(self, request):
#         appointments = Appointment.objects.all()
#         serializer = AppointmentSerializer(appointments, many=True)
#         return Response(serializer.data)

from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment ,Doctor
from .serializers import AppointmentSerializer ,DoctorsSerializer
from rest_framework import viewsets

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer