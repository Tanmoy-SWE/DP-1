from django.contrib import admin
from .models import Admin, Course_Coordinator, Course_Instructor, Semester, Course_Session, Department, Course, Program_Outcome

# Register your models here.
admin.site.register(Admin)
admin.site.register(Course_Coordinator)
admin.site.register(Course_Instructor)
admin.site.register(Semester)
admin.site.register(Course_Session)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Program_Outcome)
