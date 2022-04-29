from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class DoctorProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(default="Dr Bezos Mike", max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=90)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    rating = models.IntegerField()
    pricings = models.CharField(default="$1000- $3500", max_length=15)
    schedule = models.CharField(default="Monday, Friday, Saturday", max_length=200)
    specialties = models.CharField(default="Cosmology ChildCare ", max_length=900) 
    myeducation = models.CharField(default="Bsc Anatomy", max_length=300)
    myexperience = models.CharField(default="nurse at BlueCare", max_length=300)
    def __str__(self):
        return str(self.user.username)
    
    
class Education(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="education")
    college = models.CharField(max_length=250)
    degree = models.CharField(max_length=30)
    startDate = models.DateField(default=date.today, blank=True)
    endDate = models.DateField(default=date.today, blank=True)
    
    def __str__(self):
        return str(self.doctor)
    
class Experience(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="experience")
    experience = models.CharField(max_length=250)
    startDate = models.DateField(default=date.today, blank=True)
    endDate = models.DateField(default=date.today, blank=True)
    
    def __str__(self):
        return str(self.doctor)
    


