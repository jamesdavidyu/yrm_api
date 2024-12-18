from django.db import models
import uuid

class Name(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    input_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255)
    input_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.CharField(max_length=255)
    input_at = models.DateTimeField(auto_now_add=True)

class Hour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hour = models.DecimalField(max_digits=4, decimal_places=2)
    input_at = models.DateTimeField(auto_now_add=True)