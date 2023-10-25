from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class Employee(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    employeeId = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    presentAddress = models.CharField(max_length=255)
    contactNo = models.CharField(max_length=255)
    jwt_token = models.TextField(null=True, blank=True)
    

    username = None

    USERNAME_FIELD = 'employeeId'
    REQUIRED_FIELDS = []