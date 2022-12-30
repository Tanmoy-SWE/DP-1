from django.db import models
from Coordinator.models import AssignedCourses, Program_Outcome

# Create your models here.
class Course_Outcome(models.Model):
    c_code = models.CharField(max_length = 200, default=None)
    description = models.TextField(max_length = 300, default=None)
    total_marks = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    course_assigned = models.ForeignKey(AssignedCourses, on_delete = models.CASCADE)
    is_active = models.BooleanField(default=False)


class Mapping(models.Model):
     program_outcome = models.ForeignKey(Program_Outcome, on_delete = models.CASCADE)
     course_outcome = models.ForeignKey(Course_Outcome, on_delete=models.CASCADE)     
     course_assigned = models.ForeignKey(AssignedCourses, on_delete = models.CASCADE)
    
class PdfFiles(models.Model):
    name = models.CharField(max_length=500, default=None)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

class Student(models.Model):
    student_id = models.CharField(max_length = 20, default=None)
    student_name = models.CharField(max_length = 100, default=None)
    a_year = models.CharField(max_length=20, default = None)
    course_assigned = models.ForeignKey(AssignedCourses, on_delete=models.CASCADE)

class Questions(models.Model):

    number = models.IntegerField()
    subsection = models.CharField(max_length=2, default=None)
    totalmarks = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    description = models.TextField(max_length = 3000, default=None)
    type = models.CharField(max_length = 20, default=None)
    course_outcome = models.ForeignKey(Course_Outcome, on_delete=models.CASCADE, null=True)
    course_assigned = models.ForeignKey(AssignedCourses, on_delete=models.CASCADE, default=None)

class Result(models.Model):
    totalmarks = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    marks_obtained = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, default=None)
    course_assigned = models.ForeignKey(AssignedCourses, on_delete=models.CASCADE, default=None)
    course_outcome = models.ForeignKey(Course_Outcome, on_delete=models.CASCADE, default=None, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)

class Threshold(models.Model):
    course_assigned = models.ForeignKey(AssignedCourses, on_delete=models.CASCADE)
    individual = models.DecimalField(max_digits = 6, decimal_places = 2, default=50)
    overall = models.DecimalField(max_digits = 6, decimal_places = 2, default=50)
    program = models.DecimalField(max_digits = 6, decimal_places = 2, default=50)