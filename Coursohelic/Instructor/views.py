from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Coordinator.models import AssignedCourses, Program_Outcome, Course
from .models import Course_Outcome, Mapping, Assigned_CO
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
    course_assigned = AssignedCourses.objects.get(id = pk)
    co = Course_Outcome.objects.filter(course_assigned = course_assigned)
    assigned_co = []
    for i in range(0, len(co)):
        a = Assigned_CO.objects.filter(co = co[i])
        for i in range(0, len(a)):
            assigned_co.append(a[i])

    print(type(assigned_co[i]))
    context = {'assigned': assigned_co}
    return render(request, "Program Instructor/EditCourse.html", context)

# def instructorList(request):
#    instructors = instructor.objects.all()
#    instrList = []
#    for i in range(0,len(instructors)):
#        if (instructors[i].created_by == request.user):
#                instrList.append(instructors[i])
 
#    print(instrList)
#    context = {'instructors': instrList}
#    return render(request, 'Program Coordinator/InstructorList.html', context)

def addCO(request, pk, pk2):
    co = Course_Outcome.objects.get(id = pk2)
    course_assigned = AssignedCourses.objects.get(id = pk)
    name_c = Course_Outcome.objects.filter(course_assigned = course_assigned)

    length = len(name_c) + 1
    p_number = "CO" + str(length)   
    assign = Course_Outcome(c_code = p_number, description = co.description, total_marks = co.total_marks, course_assigned = course_assigned)
    assign.save()

    course_info = course_assigned.course
    coordinator_info = course_info.created_by
    program_assigned = Assign_Program.objects.filter(coordinator = coordinator_info)
    program = program_assigned[0].program

    p_outcome = Program_Outcome.objects.filter(program = program)
    print(p_outcome)
    for i in range(0, len(p_outcome)):
        assign2 = Mapping(program_outcome = p_outcome[i], course_outcome = assign, weight = 0, course_assigned= course_assigned)
        assign2.save()
    
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


def Merge_pdf(f):
    #Create and instance of PdfFileMerger() class
    merger = PdfFileMerger()
    #Create a list with file names
    #files = ['file1.pdf','file2.pdf','pdf3.pdf']
    pdf_files = []
    for i in range(0, len(f)):
        pdf_files.append(settings.MEDIA_ROOT+'/'+f[i])
    #Iterate over the list of file names
    for pdf_file in pdf_files:
        #Append PDF files
        merger.append(pdf_file)
    #Write out the merged PDF
    merger.write("merged_3_pages.pdf")
    merger.close()
    

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
    file_list = []
    if request.method == 'POST':
        for q in list_of_questions:
                request_file = request.FILES[q]
                fs = FileSystemStorage()
                file_list.append(str(request_file))
                fs.save(request_file.name, request_file)
    Merge_pdf(file_list)
    context = {
        'list_of_questions' : list_of_questions,
    }
    return render(request, "Program Instructor/CourseFileGenerator.html", context=context)