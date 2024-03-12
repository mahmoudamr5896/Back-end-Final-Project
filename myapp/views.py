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

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment, Review
from .serializers import AppointmentSerializer, ReviewSerializer 
from rest_framework import viewsets

class AppointmentListView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        appointment = self.get_object(pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get_object(self, pk):
    #     try:
    #         return Appointment.objects.get(pk=pk)
    #     except Appointment.DoesNotExist:
    #         raise Http404
 
 

class ReviewFunBaseView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()