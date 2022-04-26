from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    BLOOD_GROUP = [
        ('A','A'),
        ('B','A'),
        ('AB','AB'),
        ('O','O')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=120)
    age = models.IntegerField()
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return str(self.user)
