# Create your models here.
from django.db import models
class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=100)
    phone =models.IntegerField()
    email=models.EmailField()
    
