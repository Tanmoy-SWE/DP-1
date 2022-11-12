from django.contrib import admin
from .models import Mapping, Course_Outcome, PdfFiles, Questions, Students

# Register your models here.
admin.site.register(Mapping)
admin.site.register(Course_Outcome)
admin.site.register(PdfFiles)
admin.site.register(Questions)
admin.site.register(Students)