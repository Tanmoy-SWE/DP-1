from asyncio.windows_events import NULL
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
    name = models.CharField(max_length=500, default=NULL)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    c_code = models.ForeignKey(Course_Outcome, on_delete=models.CASCADE)
    
class Questions(models.Model):
    c_code = models.ForeignKey(Course_Outcome, on_delete=models.CASCADE)
    total_marks = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    exam_type = models.CharField(max_length=100, default=None)

class Students(models.Model):
    c_code = models.ForeignKey(Course_Outcome, on_delete= models.CASCADE)
    name = models.CharField(max_length=300, default=NULL)
    id = models.CharField(max_length=20, default=NULL)
    program = models.CharField(max_length=100, default=NULL)
    semester = models.IntegerField(default=0)


