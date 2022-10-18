from django.db import models
from Authentication.models import User


# Create your models here.
class Course(models.Model):
    c_id = models.AutoField(primary_key = True)
    c_code = models.CharField(max_length = 200, default=None)
    c_name = models.CharField(max_length = 200, default=None)
    total_credit = models.FloatField(default=0)
    description = models.TextField(max_length = 300, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
