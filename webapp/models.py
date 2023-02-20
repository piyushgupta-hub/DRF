import email
from django.db import models
from django.forms import EmailField

class employees(models.Model):
    firstname =models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    emp_id =models.IntegerField()
    
    def __str__(self):
        return self.firstname


