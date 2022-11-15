from django.contrib import admin
from .models import Course, AssignedCourses, Program_Outcome

# Register your models here.
admin.site.register(Course)
admin.site.register(AssignedCourses)
admin.site.register(Program_Outcome)