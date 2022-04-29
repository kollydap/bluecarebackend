from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class MyAccountManager(BaseUserManager):
#     def create_user(self,email,username,password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError("Users must have username")
        
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
    
#     def create_superuser(self,email,username,password):
#         user = self.create_user(
#             email= self.normalize_email(email),
#             password = password,
#             username = username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user    
    
# class Account(AbstractBaseUser):

# @receiver(post_save, sender=User)
# def create_auth_token(sender,instance=None, created=False, **kwargs):
#       if created:
#           Token.objects.create(user=instance)
    
