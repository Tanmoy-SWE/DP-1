
from unittest.util import _MAX_LENGTH
from django.db import models
from Authentication.models import User
from django.utils import timezone

# Create your models here.

class Program(models.Model):
    p_id = models.AutoField(primary_key = True)
    p_name = models.CharField(max_length = 200, default=None)
    department = models.CharField(max_length = 200)
    total_credit = models.IntegerField()
    description = models.TextField(max_length = 300, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
class All_Coordinators(models.Model):
    coordinator = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    isAssigned = models.BooleanField(default=False)
   
class Assign_Program(models.Model):
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    
from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]