
from rest_framework import serializers
from .models import DoctorProfile,Education,Experience

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields = '__all__'
        
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    education = EducationSerializer(read_only = True, many=True)
    experience = ExperienceSerializer(read_only = True, many=True)
    class Meta:
        model = DoctorProfile
        fields = '__all__'