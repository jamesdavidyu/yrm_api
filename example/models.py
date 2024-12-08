from django.db import models
from django.contrib.auth.models import User

class User(User):
    first_name = ''
    last_name = ''
    email = ''
    _is_staff = False
    _is_superuser = False
