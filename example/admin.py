from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Name)
admin.site.register(models.Category)
admin.site.register(models.Note)
admin.site.register(models.Hour)