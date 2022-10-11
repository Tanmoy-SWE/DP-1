from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login, name='ProgramInstructorLoginPage'),
    path('ProgramInstructorRegistrationPage/', views.registration, name='ProgramInstructorRegistrationPage'),
]