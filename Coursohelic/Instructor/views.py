from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Coordinator.models import AssignedCourses

# Create your views here.
def login(request):
    return render(request , 'ProgramInstructorLoginPage.html')
def registration(request):
    return render(request , 'ProgramInstructorRegistrationPage.html')

def instructorHome(request):
   return render(request, 'Program Instructor/InstructorHome.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def course_list(request):
    
    c1 = AssignedCourses.objects.filter(instructor = request.user)
    context = {"courses": c1}
    return render(request, 'Program Instructor/AssignedCourse.html', context)


# def instructorList(request):
#    instructors = instructor.objects.all()
#    instrList = []
#    for i in range(0,len(instructors)):
#        if (instructors[i].created_by == request.user):
#                instrList.append(instructors[i])
 
#    print(instrList)
#    context = {'instructors': instrList}
#    return render(request, 'Program Coordinator/InstructorList.html', context)