from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Coordinator.models import AssignedCourses, Program_Outcome, Course
from .models import Course_Outcome, Mapping
from InstitutionAdmin.models import Assign_Program
from PyPDF4 import PdfFileMerger
from django.core.files.storage import FileSystemStorage
from django.conf import settings


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

def setCO(request, pk):
    
    a_course = AssignedCourses.objects.get(id = pk)
    course = Course.objects.get(c_id = a_course.course.c_id)
    creator = course.created_by
    program = Assign_Program.objects.get(coordinator = creator)
    program_outcomes = Program_Outcome.objects.filter(program = program.program)
    print(program_outcomes)

    course_outcomes = Course_Outcome.objects.filter(course_assigned = a_course)
    
    #if (a_course.is_mapped == True):





    context = {"course" : a_course, "poutcomes": program_outcomes, "coutcomes" : course_outcomes, "pk": pk}
    return render(request, "Program Instructor/EditCourse.html", context)


def addCO(request, pk):
    if request.method == 'POST':
        description = request.POST['course']
        course = AssignedCourses.objects.get(id = pk)
        course_outcomes = Course_Outcome.objects.filter(course_assigned = course)
        text = "CO" + str(len(course_outcomes) + 1)
        temp = Course_Outcome(c_code = text, description = description, course_assigned = course)
        temp.save()
    
    return redirect('/instructor/setCO/' + str(pk) + '/')

def deleteCO(request, pk, pk2):
   co = Course_Outcome.objects.get(id = pk2)
   co.delete()
   course_assigned = AssignedCourses.objects.get(id = pk)
   name_c = Course_Outcome.objects.filter(course_assigned = course_assigned)   

   for i in range(0, len(name_c)):
      length = i + 1
      p_number = "CO" + str(length)
      name_c[i].c_code = p_number
      name_c[i].save()

   return redirect('/instructor/setCO/' + str(pk) + '/')
    

def generateCourseFile(request):
    list_of_questions = ["Quiz1", "Quiz2"]
    questions = {
        "Quiz-1" : "",
        "Quiz-2" : "",
        # "Quiz-3" : "",
        # "Mid"    : "", 
        # "Attendance": "",
        # 'Final' : ""
    }
    if request.method == 'POST':
        merger = PdfFileMerger()
        for q in list_of_questions:
                request_file = request.FILES[q]
                merger.append(request_file)
        merger.write("static/PDFs/merged_PDFS.pdf")
        merger.close()
    context = {
        'list_of_questions' : list_of_questions,
    }
    return render(request, "Program Instructor/CourseFileGenerator.html", context=context)

def downloadCourseFile(request):
    return render(request, "Program Instructor/downloadCourseFile.html")