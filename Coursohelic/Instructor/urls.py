from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('courseInstructorForm/', views.cour_ins_form, name='courseInstructorForm'),
]