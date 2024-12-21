# example/views.py
from datetime import datetime

from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from . import models
from . import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db import connection
from .decorators import google_auth_required

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

@api_view(['POST'])
def signup(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def login(request):
    serializer = serializers.LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@google_auth_required
def hours(request):
    data = models.Hour.objects.all().order_by('hour')
    serializer = serializers.HoursSerializer(data, many=True)
    return Response({'hours': serializer.data})