from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('ProgramCoordinatorList/', views.CoordinatorList, name='CoordinatorList'),
    path('ProgramList/', views.ProgramList, name='ProgramList'),
    # path('courseInstructorForm/', views.cour_ins_form, name='courseInstructorForm'),
    # path('coordinatorForm/', views.coordinator, name='coordinatorForm'),
]