from django.db import models
from employee.models import Employee
import uuid

# Create your models here.

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def creator_name(self):
        return self.created_by.fullname

class Menu(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,  editable=False)
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menus/')

    def creator_name(self):
        return self.created_by.fullname
    
    def restaurent_name(self):
        return self.restaurant.name

    
#vote
class Vote(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,  editable=False)
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    choice = models.PositiveSmallIntegerField(choices=[(0, 'No'), (1, 'Yes')])

#Result
class Result(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    date = models.DateField()
    winner = models.ForeignKey(Restaurant, on_delete=models.CASCADE)