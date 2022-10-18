from django.contrib import admin

from InstitutionAdmin.models import All_Coordinators, Assign_Program, Program
from InstitutionAdmin.views import coordinator_list

# Register your models here.
admin.site.register(Program)
admin.site.register(Assign_Program)
admin.site.register(All_Coordinators)