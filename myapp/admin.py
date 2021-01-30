from django.contrib import admin

# Register your models here.
from .models import Student

# Dang ki model voiws admin
admin.site.register(Student)
