from django.contrib import admin
from .models import Mapping, Course_Outcome, PdfFiles

# Register your models here.
admin.site.register(Mapping)
admin.site.register(Course_Outcome)
admin.site.register(PdfFiles)