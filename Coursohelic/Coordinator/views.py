

from site import USER_SITE
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import AssignedCourses, Course
from Authentication.models import User
from InstitutionAdmin.models import All_Coordinators
# Create your views here.
 
def login(request):
   return render(request , 'ProgramCoordinatorLoginPage.html')
 
def registration(request):
   return render(request , 'ProgramCoordinatorRegistrationPage.html')
 
def coordinatorHome(request):
   coordinator = All_Coordinators.objects.get(coordinator=request.user)
   if coordinator.isAssigned == True:
      return render(request, 'Program Coordinator/CoordinatorHome.html')
   return render(request, 'Program Coordinator/NotVerified.html')
 
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
 
def delete_course(request, pk):
       course = Course.objects.get(c_id = pk)
       course.delete()
       return redirect('/coordinator/courseList')

def instructor_list(request):
   instructor = User.objects.filter(institution = request.user.institution, is_instructor = True)
   print(instructor)
   context = {'instructor': instructor}
   return render(request, 'Program Coordinator/InstructorList.html', context)

def assign_instructor(request):
         courses = Course.objects.all()
         instructors = User.objects.all()
         if request.method == "POST":
            course = request.POST['choice']
            instr = request.POST['choice2']
            c1 = Course.objects.get(c_name = course)
            c2 = User.objects.get(id = instr)
            
            
            assign = AssignedCourses(course = c1, instructor = c2)
            assign.save()
            return redirect("/coordinator/")
      
      
      
         context = {'courses' : courses , 'instructors' : instructors}
         return render(request, 'Program Coordinator/AssignCourse.html', context)

