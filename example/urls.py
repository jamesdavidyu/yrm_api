# example/urls.py
from django.urls import path
import os
from dotenv import load_dotenv

from example.views import index
from example.views import signup
from example.views import login

load_dotenv()
prefix = os.getenv('PREFIX')

urlpatterns = [
    path('', index),
    path(prefix + 'auth/signup/', signup),
    path(prefix + 'auth/login/', login)
]