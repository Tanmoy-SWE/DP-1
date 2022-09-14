

# Create your models here.
from django.db import models
import hashlib

# Create your models here.
class Admin(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=200)
    insititution = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=12)
    username = models.CharField(max_length=60)
    password = hashlib.sha256(models.CharField(max_length=60).encode('utf-8')).hexdigest()
    
    


class Course_Coordinator(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=200)
    insititution = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=12)
    username = models.CharField(max_length=60)
    password = hashlib.sha256(models.CharField(max_length=60).encode('utf-8')).hexdigest()


class Course_Instructor(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=200)
    insititution = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=12)
    username = models.CharField(max_length=60)
    password = hashlib.sha256(models.CharField(max_length=60).encode('utf-8')).hexdigest()