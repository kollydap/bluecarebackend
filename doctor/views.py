from rest_framework import generics
from .models import DoctorProfile
from .serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class DoctorList(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated]
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer