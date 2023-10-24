from django.db import models
from employee.models import Employee

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def creator_name(self):
        return self.created_by.fullname
