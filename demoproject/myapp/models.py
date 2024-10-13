from django.db import models

# Create your models here.


class Employees(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(max_length=10)
    age = models.IntegerField(max_length=10)
    place = models.CharField(max_length=100)
