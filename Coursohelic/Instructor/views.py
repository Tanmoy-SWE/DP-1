from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Coordinator.models import AssignedCourses, Program_Outcome, Course
from .models import Course_Outcome, Mapping
from InstitutionAdmin.models import Assign_Program
#from PyPDF4 import PdfFileMerger
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import json

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
    

    course_outcomes = Course_Outcome.objects.filter(course_assigned = a_course)
    # ismapped = [[False] * len(program_outcomes) for i in range(len(course_outcomes))]
    ismapped = {}
    for i in range(0, len(course_outcomes)):
        newmap = {}
        for j in range(0, len(program_outcomes)):
            temp = Mapping.objects.filter(course_outcome = course_outcomes[i], program_outcome = program_outcomes[j])
            if (len(temp) > 0):
                newmap[program_outcomes[j].id] = True
            else:
                newmap[program_outcomes[j].id] = False 
        ismapped[course_outcomes[i].id] = newmap

    ticked = []
    print(ismapped)
    for i in range(0, len(course_outcomes)):
           for j in range(0, len(program_outcomes)):
             temp = Mapping.objects.filter(course_outcome = course_outcomes[i], program_outcome = program_outcomes[j])
            
             if (len(temp)> 0):
                
                 #ismapped.append(True)
                 ticked.append([course_outcomes[i].id, program_outcomes[j].id])
    
    # ticked = []
    # r = 0
    # c = 0
    # for x in ismapped:
    #     r = r + 1
    #     for y in ismapped[x]:
    #         c = c + 1
    #         if ismapped[x][y] == True:
    #             ticked.append([r,c])
    #     c = 1
    # print(ticked)                



    

    
    
    #if (a_course.is_mapped == True):





    context = {"course" : a_course, "poutcomes": program_outcomes, "coutcomes" : course_outcomes, "pk": pk, "ismapped": ismapped, "ticked": ticked}
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
    
def non_activate_course(pk):
    assigned_course = AssignedCourses.objects.get(id = pk)
    courses = Course_Outcome.objects.filter(course_assigned = assigned_course)
    for i in range(0, len(courses)):
        courses[i].is_active = False
        courses[i].save()

def delete_mapping(pk):
    assigned_course = AssignedCourses.objects.get(id = pk)
    temp = Mapping.objects.filter(course_assigned = assigned_course)
    for i in range(0, len(temp)):
        temp[i].delete()

def submitmap(request, pk):
    delete_mapping(pk)
    non_activate_course(pk)

    checkactive = request.POST.getlist('checkactive')
    

    
    for i in range(0, len(checkactive)):
        num = int(checkactive[i])
        print(num)
        temp = Course_Outcome.objects.get(id = num)
        temp.is_active = True
        temp.save()
    
    mapper = request.POST.getlist('mapper')
    print(mapper)
    for i in range(0, len(mapper)):
        mapper[i] = mapper[i].split("s")
    print(mapper)
    c_assigned = AssignedCourses.objects.get(id = pk)
    for j in range(0, len(mapper)):
        co = Course_Outcome.objects.get(id = int(mapper[j][0]))
        po = Program_Outcome.objects.get(id = int(mapper[j][1]))
        map = Mapping(program_outcome = po, course_outcome = co, course_assigned = c_assigned)
        map.save()

    print(mapper)    

    

    
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