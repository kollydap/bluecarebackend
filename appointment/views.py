from .models import Appointment
from rest_framework import generics
from .serializers import AppointmentSerializer
from rest_framework.permissions import BasePermission,IsAdminUser,IsAuthenticated, AllowAny

# class AppointmentUpdatePermission(BasePermission):
#     message = 'How the hell did you even get here hun :('
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.patient == request.user

#Only my admin can see all appointments created by all users and doctors :)
#the user needs to be allowed to see lists of his appointments
#! reminder : you'll filter through it
# TODO
#? To ask a question
# * important comment

class AppointmentList(generics.ListAPIView):
    permission_classes= [IsAdminUser]
    queryset =  Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pass

#only Authenticated people should be able to create an Appointment :}
class AppointmentCreate(generics.CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset =  Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pass

#Every Appointment detail, should only be visible to the doctor and patient involved, maybe the admin too
class AppointmentDetail(generics.RetrieveDestroyAPIView):
    permission_classes =[IsAuthenticated]
    queryset =  Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pass
