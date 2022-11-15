from django.db import models
from Coordinator.models import AssignedCourses, Program_Outcome, Course

# Create your models here.
class Course_Outcome(models.Model):
    c_code = models.CharField(max_length = 200, default=None)
    description = models.TextField(max_length = 300, default=None)
    total_marks = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    course_assigned = models.ForeignKey(AssignedCourses, on_delete = models.CASCADE)

class Assigned_CO(models.Model):
    co = models.ForeignKey(Course_Outcome, on_delete = models.CASCADE)
    is_assigned = models.BooleanField(default=True)

class Mapping(models.Model):
     program_outcome = models.ForeignKey(Program_Outcome, on_delete = models.CASCADE)
     course_outcome = models.ForeignKey(Assigned_CO, on_delete = models.CASCADE)
     weight = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
     course_assigned = models.ForeignKey(AssignedCourses, on_delete = models.CASCADE)
    
class PdfFiles(models.Model):
    name = models.CharField(max_length=500, default=None)
    filepath= models.FileField(upload_to='images/', null=True, verbose_name="")
    #co_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    
