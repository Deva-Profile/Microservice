from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserloginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

      
        userlogin = Userlogin.objects.create(user=user, phone=self.context['request'].data['phone'])
        return user
    

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True)

