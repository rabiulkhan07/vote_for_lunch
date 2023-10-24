from django.db import models
from employee.models import Employee

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def creator_name(self):
        return self.created_by.fullname

class Menu(models.Model):
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
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    choice = models.PositiveSmallIntegerField(choices=[(0, 'No'), (1, 'Yes')])

#Result
class Result(models.Model):
    date = models.DateField()
    winner = models.ForeignKey(Restaurant, on_delete=models.CASCADE)