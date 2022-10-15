from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    is_admin= models.BooleanField(default=True)
    is_coordinator = models.BooleanField(default=False)
    institution = models.CharField(max_length=200,default='')