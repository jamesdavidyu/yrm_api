from rest_framework import serializers
from . import models
from datetime import datetime
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = '',
            last_name = '',
            email = '',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            date_joined = datetime.now(),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        else:
            User.objects.filter(username=username).update(last_login=datetime.now())
            data['user'] = user
            return data