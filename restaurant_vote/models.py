from django.db import models
from employee.models import Employee

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.DateField()
    items = models.TextField()

class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(Employee, on_delete=models.CASCADE) 
