from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.coordinatorHome, name='ProgramCoordinatorHomePage'),
     path('logout/', views.logout_user, name='logout'),
     path('courseList/', views.coursesList, name='courseList'),
     
     
]