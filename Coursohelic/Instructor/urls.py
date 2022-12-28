from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.instructorHome, name='ProgramInstructorHome'),
    path('logout/', views.logout_user, name='logout'),
    path('courseList/', views.course_list, name="course_list"),
    path('setCO/<pk>/', views.setCO, name = "setCO"),
    path('addCO/<pk>/', views.addCO, name="addCO"),
    path('deleteCO/<pk>/<pk2>/', views.deleteCO, name="deleteCO"),
    path('generateCourseFile/', views.generateCourseFile, name="generateCourseFile"),
    path('downloadCourseFile/', views.downloadCourseFile, name="downloadCourseFile"),
    path('submitmap/<pk>/', views.submitmap, name="submitmap"),
    path('confirmmap/<pk>/', views.confirmmap, name="confirmmap"),
    path('lockmapping/<pk>/', views.lockmapping, name="lockmapping")
    

  #  path('courseList/', views.instructorList, name='instructorList'),
]