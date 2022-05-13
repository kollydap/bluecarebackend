from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        # i'm using the default django user model
        model = User
        fields = '__all__'
        # fields = ('email', 'username','password')
        extra_kwargs = {'password':{'write_only':True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance  = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        # i'm using the default django user model
        model = User
        fields = '__all__'
        # fields = ('email', 'username','password')