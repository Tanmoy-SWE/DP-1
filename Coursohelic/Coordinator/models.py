from django.db import models
from Authentication.models import User
from InstitutionAdmin.models import Program
from distutils.command.upload import upload
 
# Create your models here.
class Course(models.Model):
   c_id = models.AutoField(primary_key = True)
   c_code = models.CharField(max_length = 200, default=None)
   c_name = models.CharField(max_length = 200, default=None)
   total_credit = models.FloatField(default=0)
   description = models.TextField(max_length = 300, default=None)
   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
   is_assigned = models.BooleanField(default = False)
  
 
class Program_Outcome(models.Model):
   c_code = models.CharField(max_length = 200, default=None)
   description = models.TextField(max_length = 300, default=None, null=True)
   program = models.ForeignKey(Program, on_delete=models.CASCADE)


class AssignedCourses(models.Model):
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
      instructor = models.ForeignKey(User, on_delete=models.CASCADE)
      is_mapped = models.BooleanField(default=False)
      

