# example/urls.py
from django.urls import path

from example.views import index
from example.views import signup
from example.views import login

urlpatterns = [
    path('', index),
    path('api/v1/auth/signup/', signup),
    path('api/v1/auth/login/', login)
]