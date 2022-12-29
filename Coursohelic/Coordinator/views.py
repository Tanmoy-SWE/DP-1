

from site import USER_SITE
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import AssignedCourses, Course, Program_Outcome
from Instructor.models import Course_Outcome
from Authentication.models import User
from InstitutionAdmin.models import All_Coordinators, Assign_Program, Program
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
         courses = Course.objects.filter(created_by = request.user)
         instructors = User.objects.filter(institution = request.user.institution, is_instructor = True)
         if request.method == "POST":
            course = request.POST['choice']
            instr = request.POST['choice2']
            c1 = Course.objects.get(c_name = course, created_by = request.user)
            c2 = User.objects.get(id = instr)
            
            
            assign = AssignedCourses(course = c1, instructor = c2)
            assign.save()


            return redirect("/coordinator/")
      
      
      
         context = {'courses' : courses , 'instructors' : instructors}
         return render(request, 'Program Coordinator/AssignCourse.html', context)

def confirm_course(request, pk):
   context = {"pk": pk}
   return render(request, "Program Coordinator/DeleteConfirmationCourse.html", context)

def go_back_course(request):
   return redirect("/coordinator/courseList/")

def setPO(request):
      program_assigned = Assign_Program.objects.get(coordinator = request.user)
      print(program_assigned.program)
      p_name = Program_Outcome.objects.filter(program = program_assigned.program)
      
      
      program_assigned2 = Program.objects.filter(p_name = program_assigned.program.p_name).exclude(p_id = program_assigned.program.p_id)
      p_name2 = []
      for i in range(0, len(program_assigned2)):
             temp1 = Program_Outcome.objects.filter(program = program_assigned2[i])
             for j in range(len(temp1)):
                    p_name2.append(temp1[j])
         
      if request.method == "POST":
            p_outcome = request.POST['program']
            
            length = len(p_name) + 1
            
            p_number = "PO" + str(length)   
      
            assign = Program_Outcome(c_code = p_number, description = p_outcome, program = program_assigned.program)
            assign.save()
            return redirect("/coordinator/setPO")
   
      return render(request, 'Program Coordinator/EditProgram.html', {"CurrentProgram": p_name, "ExistingProgram": p_name2, "program" : program_assigned.program})

def editPO(request, pk):
       if request.method == "POST":
             description = request.POST['program']
             temp = Program_Outcome.objects.get(id = pk)
             temp.description = description
             temp.save()

             return redirect("/coordinator/setPO")


       new = Program_Outcome.objects.get(id = pk)
       context = {"pk": new}
       return render(request, "Program Coordinator/AddPO.html", context)


def addPO(request, pk):
   po = Program_Outcome.objects.get(id = pk)
   program_assigned = Assign_Program.objects.get(coordinator = request.user)
   p_name = Program_Outcome.objects.filter(program = program_assigned.program)   

   length = len(p_name) + 1
   p_number = "PO" + str(length)
   assign = Program_Outcome(c_code = p_number, description = po.description, program = program_assigned.program)
   assign.save()
   return redirect("/coordinator/setPO")


def deletePO(request, pk):
   po = Program_Outcome.objects.get(id = pk)
   po.delete()
   program_assigned = Assign_Program.objects.get(coordinator = request.user)
   p_name = Program_Outcome.objects.filter(program = program_assigned.program)   

   for i in range(0, len(p_name)):
      length = i + 1
      p_number = "PO" + str(length)
      p_name[i].c_code = p_number
      p_name[i].save()

   return redirect("/coordinator/setPO")
   
