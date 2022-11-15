from django.db import models
from Coordinator.models import AssignedCourses, Program_Outcome

# Create your models here.
class Course_Outcome(models.Model):
    c_code = models.CharField(max_length = 200, default=None)
    description = models.TextField(max_length = 300, default=None)
    total_marks = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    course_assigned = models.ForeignKey(AssignedCourses, on_delete = models.CASCADE)
class Mapping(models.Model):
     program_outcome = models.ForeignKey(Program_Outcome, on_delete = models.CASCADE)
     course_outcome = models.ForeignKey(Course_Outcome, on_delete = models.CASCADE)
     weight = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
     course_assigned = models.ForeignKey(AssignedCourses, on_delete = models.CASCADE)
    
class PdfFiles(models.Model):
    name = models.CharField(max_length=500, default=None)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
