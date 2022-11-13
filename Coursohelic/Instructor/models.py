from django.db import models
from Coordinator.models import AssignedCourses, Program_Outcome, Course

# Create your models here.
class Course_Outcome(models.Model):
    c_code = models.ForeignKey(Course, on_delete=models.CASCADE),
    co_id = models.CharField(max_length=20, default="CO1")
    description = models.TextField(max_length = 300, default=None)
    total_marks = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)


class Mapping(models.Model):
    program_outcome = models.ForeignKey(Program_Outcome, on_delete = models.CASCADE)
    co_id = models.ForeignKey(Course_Outcome, on_delete = models.CASCADE)
    weight = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    course_assigned = models.ForeignKey(AssignedCourses, on_delete = models.CASCADE)
    
class PdfFiles(models.Model):
    name = models.CharField(max_length=500, default=None)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    c_code = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True)
    
class Questions(models.Model):
    co_id = models.ForeignKey(Course_Outcome, on_delete = models.CASCADE)
    question_no = models.IntegerField(default=0)
    total_marks = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    exam_type = models.CharField(max_length=100, default=None)

class Students(models.Model):
    c_code = models.ForeignKey(Course, on_delete= models.CASCADE)
    name = models.CharField(max_length=300, default=None)
    student_id = models.CharField(max_length=20, default=None)
    program = models.CharField(max_length=100, default=None)
    semester = models.IntegerField(default=0)