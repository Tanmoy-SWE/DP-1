from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('AdminLogin/', views.adminlogin, name='adminlogin'),
    path('AdminRegistrationPage/', views.adminauth, name='adminauth'),
    path('CoordinatorLogin/', views.coordinatorlogin, name='coordinatorlogin'),
    path('CoordinatorRegistrationPage/', views.coordinatorauth, name='coordinatorauth'),
    path('InstructorLogin/', views.instructorlogin, name='instructorlogin'),
    path('InstructorRegistrationPage/', views.instructorauth, name='instructorauth'),
    
]