from django.contrib import admin
from .models import Semester, Course_Session, Course, Program_Outcome

# Register your models here.

admin.site.register(Semester)
admin.site.register(Course_Session)

admin.site.register(Course)
admin.site.register(Program_Outcome)

