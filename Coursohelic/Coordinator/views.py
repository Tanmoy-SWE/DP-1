

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Course
 
# Create your views here.
 
def login(request):
   return render(request , 'ProgramCoordinatorLoginPage.html')
 
def registration(request):
   return render(request , 'ProgramCoordinatorRegistrationPage.html')
 
def coordinatorHome(request):
   return render(request, 'Program Coordinator/CoordinatorHome.html')
 
def logout_user(request):
   logout(request)
   return redirect('/')
 
def coursesList(request):
   courses = Course.objects.all()
   courList = []
   for i in range(0,len(courses)):
       if (courses[i].created_by == request.user):
               courList.append(courses[i])
 
   print(courList)
   context = {'courses': courList}
   return render(request, 'Program Coordinator/CourseList.html', context)
 
def addCourse(request):
  
   if request.method == 'POST':
       user = request.user
       print(user)
       courseCode = request.POST['Course_code']
       courseName = request.POST['Course_name']
       desc = request.POST['desc']
       credit = request.POST['total_credit']
       print(courseCode)
       new_course = Course(c_code = courseCode, c_name = courseName, total_credit= credit,
                           description=desc, created_by=user)
       new_course.save()
       return redirect('/coordinator/courseList/')
  
   return render(request, 'Program Coordinator/AddCourse.html')
 

