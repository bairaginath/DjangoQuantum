from django.db import models

__author__ = 'bairagi'




class UserDB(models.Model):
      email=models.EmailField(max_length=255,unique=True)
      password=models.CharField(max_length=255)
      firstName=models.CharField(max_length=255,null=True)
      lastName=models.CharField(max_length=255,null=True)

