

# Create your models here.
from django.db import models
import hashlib

# Create your models here.


class Semester(models.Model):
    id = models.CharField(max_length = 20, primary_key=True)
    semester_name = models.CharField(max_length=200)
    semester_length = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Course(models.Model):
    c_id = models.CharField(max_length = 20, primary_key=True)
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    #department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)

class Course_Session(models.Model):
    csid = models.CharField(max_length = 20, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    #coordinator = models.ForeignKey(Course_Coordinator, on_delete=models.SET_NULL, blank=True, null=True)
    #instructor = models.ForeignKey(Course_Instructor, on_delete=models.SET_NULL, blank=True, null=True)
    section = models.CharField(max_length=20)
    total_CO_marks = models.BigIntegerField()


class Program_Outcome(models.Model):
    p_id = models.CharField(max_length = 20, primary_key=True)
    description = models.CharField(max_length=1000)
    #department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)