from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.coordinatorHome, name='ProgramCoordinatorHomePage'),
     path('logout/', views.logout_user, name='logout'),
     path('courseList/', views.coursesList, name='courseList'),
     path('addCourse/', views.addCourse, name='addCourse'),
     path('deleteCourse/<pk>', views.delete_course, name='delete_course'),
     path('instructorList/', views.instructor_list, name='instructor_list'),
     path('assignedCourses/', views.assign_instructor, name='assignedCourses'),
     path('courseConfirmation/<pk>', views.confirm_course, name="confirm_course"),
     path('goBackCourse', views.go_back_course,name="go_back_course"),
     path('setPO/', views.setPO, name='setPO'),
     path('addPO/<pk>/', views.addPO, name='addPO'),
     path('deletePO/<pk>/', views.deletePO, name='deletePO'),
     path('editPO/<pk>/', views.editPO , name="editPO")
]