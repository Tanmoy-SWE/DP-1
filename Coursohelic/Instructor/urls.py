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
    path('lockmapping/<pk>/', views.lockmapping, name="lockmapping"),
    path('studentcourselist/', views.studentcourselist, name="studentcourselist"),
    path('viewstudentlist/<pk>/', views.viewstudentlist, name="viewstudentlist"),
    path('addstudent/<pk>/', views.addstudent, name="addstudent"),
    path('deletestudentconfirmation/<pk>/<pk2>', views.deletestudentconfirmation, name="deletestudentconfirmation"),
    path('deletestudent/<pk>/<pk2>', views.deletestudent, name="deletestudent"),
    path('gobackstudentlist/<pk>/', views.gobackstudentlist, name="gobackstudentlist"),
    path('questioncourselist/', views.questioncourselist, name="questioncourselist"),
    path('viewtermlist/<pk>/', views.viewtermlist, name="viewtermlist"), 
    path('questionlist/<pk>/<str:pk2>/', views.questionlist, name="questionlist"),
    path('addquestion/<pk>/<str:pk2>/', views.addquestion, name="addquestion"),
    path('instructorProfile', views.instructorProfile, name = "instructorProfile"),
    path('deleteconfirmation/<pk>/<str:pk2>/<pk3>/', views.deleteconfirmation, name="deleteconfirmation"),
    path('deletequestion/<pk>/<str:pk2>/<pk3>/', views.deletequestion, name="deletequestion"),
    path('gobackquestionlist/<pk>/<str:pk2>/', views.gobackquestionlist, name="gobackquestionlist")
  #  path('courseList/', views.instructorList, name='instructorList'),
]