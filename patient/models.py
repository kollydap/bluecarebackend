from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    BLOOD_GROUP = [
        ('A','A'),
        ('B','A'),
        ('AB','AB'),
        ('O','O')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=120)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return str(self.user.username)

