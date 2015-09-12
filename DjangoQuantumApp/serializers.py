from rest_framework import serializers

__author__ = 'bairaginath'



class LoginSerializer(serializers.Serializer):
      email=serializers.EmailField()
      password=serializers.CharField()




class UserSerializer(serializers.Serializer):
      id=serializers.CharField(required=False,default='')
      email=serializers.EmailField()
      password=serializers.CharField()
      firstName=serializers.CharField(required=False,default='')
      lastName=serializers.CharField(required=False,default='')

