from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(AbstractUser):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    employeeId = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    presentAddress = models.CharField(max_length=255)
    contactNo = models.CharField(max_length=255)
    

    username = None

    USERNAME_FIELD = 'employeeId'
    REQUIRED_FIELDS = []