
from unittest.util import _MAX_LENGTH
from django.db import models
from Authentication.models import User

# Create your models here.

class Program(models.Model):
    p_id = models.AutoField(primary_key = True)
    p_name = models.CharField(max_length = 200, default=None)
    department = models.CharField(max_length = 200)
    total_credit = models.IntegerField()
    description = models.TextField(max_length = 300, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
class All_Coordinators(models.Model):
    coordinator = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    isAssigned = models.BooleanField(default=False)
   
class Assign_Program(models.Model):
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)