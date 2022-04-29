from rest_framework import generics
from .models import PatientProfile
from .serializers import PatientSerializer
from django.contrib.auth.models import User

class PatientList(generics.ListAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientSerializer

class PatientCreate(generics.CreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientSerializer