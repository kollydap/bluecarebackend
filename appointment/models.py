from django.db import models
from doctor.models import DoctorProfile
from patient.models import PatientProfile
from django.contrib.auth.models import User

class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    appointment_time = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    def __str__(self):
	    return str(self.appointment_time) 

# class Notification(models.Model):
# 	doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
# 	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
# 	message = models.CharField()
