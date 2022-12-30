from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Coordinator.models import AssignedCourses, Program_Outcome, Course
from .models import Course_Outcome, Mapping, Student, Questions, Result, Threshold
from InstitutionAdmin.models import Assign_Program
from PyPDF2 import PdfFileMerger
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import json
from django.http import HttpResponse

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



    

    
    
    # if (a_course.is_mapped == True):
    #     return HttpResponse("Hi")




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
    
    c_assigned = AssignedCourses.objects.get(id = pk)
    temp = Course_Outcome.objects.filter(course_assigned = c_assigned).exclude(is_active = True)
    for i in range(0, len(temp)):
        temp[i].delete()
    
    temp = Course_Outcome.objects.filter(course_assigned = c_assigned)
    for i in range(len(temp)):
        coid = "CO" + str(i + 1)
        temp[i].c_code = coid
        temp[i].save()
        #print(temp[i].c_code)

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

def confirmmap(request, pk):
    context = {"pk" : pk}
    return render(request, "Program Instructor/MapConfirmation.html", context)    

def lockmapping(request, pk):
    c = AssignedCourses.objects.get(id = pk)
    c.is_mapped = True
    c.save()

    return redirect("/instructor/courseList/")

def generateCourseFile(request):
    list_of_questions = ["Course_Outline", "Quiz1", "Quiz2", "Quiz3", "Mid", "Final", "Attendance"]
    questions = {
        "Quiz-1" : "",
        "Quiz-2" : "",
        # "Quiz-3" : "",
        # "Mid"    : "", 
        # "Attendance": "",
        # 'Final' : ""
    }
    
    print(request.POST)
    print(783273732887378)
    if request.method == 'POST':
        merger = PdfFileMerger()
        print(783273732887378)
        for q in list_of_questions:
                request_file = request.FILES[q]
                
                merger.append(request_file)
        merger.write("static/PDFs/merged_PDFS.pdf")
        merger.close()
        return redirect("downloadCourseFile")
    context = {
        'list_of_questions' : list_of_questions,
    }
    return render(request, "Program Instructor/CourseFileGenerator.html", context=context)

def downloadCourseFile(request):
    
    return render(request, "Program Instructor/downloadCourseFile.html")

def studentcourselist(request):
    
    courses_a = AssignedCourses.objects.filter(instructor = request.user)
    context = {"courses": courses_a}
    return render(request, "Program Instructor/CourseListForStudents.html", context)

def viewstudentlist(request, pk):

    getcourse = AssignedCourses.objects.get(id = pk)
    students = Student.objects.filter(course_assigned = getcourse)
    

    context = {"pk": pk, "students": students}
    return render(request, "Program Instructor/StudentList.html", context)

def addstudent(request, pk):
    getcourse = AssignedCourses.objects.get(id = pk)
    if request.method == "POST":
        name = request.POST['name']
        id = request.POST['id']
        year = request.POST['year']

        new_entry = Student(student_id = id, student_name = name, a_year = year, course_assigned = getcourse)
        new_entry.save()

        return redirect("/instructor/viewstudentlist/" + str(pk) + "/")


    context = {"pk": pk}
    return render(request, "Program Instructor/AddStudent.html", context)

def deletestudentconfirmation(request, pk, pk2):

    return render(request, "Program Instructor/DeleteStudentConfirmation.html", {"pk": pk, "pk2": pk2})

def deletestudent(request, pk, pk2):
    student = Student.objects.get(id = pk2)
    student.delete()

    return redirect("/instructor/viewstudentlist/" + str(pk) + "/")

def gobackstudentlist(request, pk):
    
    return redirect("/instructor/viewstudentlist/" + str(pk) + "/")

def questioncourselist(request):
    courses_a = AssignedCourses.objects.filter(instructor = request.user)
    context = {"courses": courses_a}
    return render(request, "Program Instructor/QuestionManagementCourseList.html", context)

def viewtermlist(request, pk):
    c_assigned = AssignedCourses.objects.get(id = pk)
    context = {"pk": pk, "course": c_assigned}
    return render(request, "Program Instructor/AllTermList.html", context)

def questionlist(request, pk, pk2):
    print(pk2)
    c_assigned = AssignedCourses.objects.get(id = pk)
    questions = Questions.objects.filter(course_assigned = c_assigned, type=pk2)
    total_marks = 0
    for i in range(0, len(questions)):
        total_marks += questions[i].totalmarks
        

    context={"pk": pk, "pk2": pk2, "course": c_assigned, "questions": questions, "total_marks": total_marks}
    return render(request, "Program Instructor/QuestionList.html", context)

def addquestion(request, pk, pk2):
    c_assigned = AssignedCourses.objects.get(id = pk)
    co = Course_Outcome.objects.filter(course_assigned = c_assigned)
    
    
    totalquestions = Questions.objects.filter(course_assigned = c_assigned, type=pk2)
    students = Student.objects.filter(course_assigned = c_assigned)
    q_number = len(totalquestions) + 1
    if request.method == "POST":
        name = request.POST["Marks"]
        description = request.POST["Description"]
        co_out = request.POST["choice"]
        print(name)
        print(description)
        print(co_out)
        print(pk2)

        co_val = Course_Outcome.objects.get(id = co_out)
        temp = Questions(number = q_number, totalmarks = name, description = description, type=pk2, course_outcome = co_val, course_assigned = c_assigned)
        temp.save()
        for i in range(0, len(students)):
            result = Result(totalmarks = temp.totalmarks, marks_obtained = 0, student = students[i], question = temp, course_assigned = c_assigned, course_outcome = co_val)
            result.save()

        return redirect("/instructor/questionlist/"+ str(pk) + "/" + str(pk2) + "/")
    
    context = {"pk": pk, "pk2": pk2, "course_outcomes": co, "q_number": q_number}
    return render(request, "Program Instructor/AddQuestion.html", context)

def instructorProfile(request):
    context = {"name" : request.user, 
               "ins": request.user.institution,
               "role" : "Instructor"}
    print(request.user.institution)
    return render(request, "Program Instructor/InstructorProfile.html", context)

def deleteconfirmation(request, pk, pk2, pk3):
    context = {"pk": pk, "pk2": pk2, "pk3": pk3}
    return render(request, "Program Instructor/DeleteQuestionConfirmation.html", context)

def gobackquestionlist(request, pk, pk2):
    context = {"pk": pk, "pk2": pk2}
    return redirect("/instructor/questionlist/"+ str(pk) + "/" + str(pk2) + "/")

def deletequestion(request, pk, pk2, pk3):
    question = Questions.objects.get(id = pk3)
    question.delete()

    c_assigned = AssignedCourses.objects.get(id = pk)
    questions = Questions.objects.filter(course_assigned = c_assigned, type = pk2)
    for i in range(len(questions)):
        questions[i].number = i + 1
        questions[i].save()
    
    return redirect("/instructor/questionlist/"+ str(pk) + "/" + str(pk2) + "/")

def markscourselist(request):

    a_courses = AssignedCourses.objects.filter(instructor = request.user)

    context = {"courses": a_courses}
    return render(request, "Program Instructor/CourseListForMarks.html", context)

def markstermlist(request, pk):
    c_assigned = AssignedCourses.objects.get(id = pk)
    context = {"pk": pk, "course": c_assigned}
    return render(request, "Program Instructor/AllTermListForMarks.html", context)

def studentlistmarks(request, pk, pk2):
    c_assigned = AssignedCourses.objects.get(id = pk)
    students = Student.objects.filter(course_assigned = c_assigned)
    question = Questions.objects.filter(course_assigned = c_assigned, type = pk2)
    totalquiz = 0
    for i in range(len(question)):
        totalquiz += question[i].totalmarks
    
    everything = []
    for i in range(len(students)):
        total_marks = 0
        for j in range(len(question)):
            result = Result.objects.filter(student = students[i], question=question[j])
            total_marks += result[0].marks_obtained
        everything.append({"student": students[i], "total_marks": total_marks, "identity": students[i].id})

    

    context = {"pk": pk, "pk2": pk2, "everything": everything, "totalmark": totalquiz, "course": c_assigned}
    return render(request, "Program Instructor/StudentListForMarks.html",context)

def assignmarks(request, pk, pk2, pk3):
    c_assigned = AssignedCourses.objects.get(id = pk)
    questions = Questions.objects.filter(course_assigned = c_assigned, type= pk2)
    student = Student.objects.get(id = pk3)
    print(questions)
    if request.method == "POST":
        for i in range(len(questions)):
            
            code = str(questions[i].number)
            
            item = request.POST[code]
            
            result = Result.objects.get(course_assigned = c_assigned, question = questions[i], student = student)
            
            item = int(item)
            if (item > result.totalmarks):
                result.marks_obtained = result.totalmarks
            elif(item < 0):
               result.marks_obtained = 0
            else:
                result.marks_obtained = item 
            
            
            result.save()
            
            
        return redirect("/instructor/studentlistmarks/" + str(pk) + "/" + str(pk2) +"/")    


    context = {"pk": pk, "pk2": pk2, "pk3": pk3, "questions": questions}
    return render(request, "Program Instructor/AssignMarks.html", context)

def cocourselist(request):
    courses_a = AssignedCourses.objects.filter(instructor = request.user)
    context = {"courses": courses_a}
    return render(request, "Program Instructor/CO templates/CourseList.html", context)

def threshold(request, pk):
    courses_a = AssignedCourses.objects.get(id = pk)
    t_hold = Threshold.objects.filter(course_assigned = courses_a)
    if (len(t_hold) == 0):
        print("Not Available")
        threshold = Threshold(course_assigned = courses_a)
        threshold.save()
    else:
        threshold = t_hold[0]

    context = {"pk": pk, "threshold": threshold}
    return render(request, "Program Instructor/CO templates/Threshold.html", context)

def assignindividualthreshold(request, pk):
    courses_a = AssignedCourses.objects.get(id = pk)
    t_hold = Threshold.objects.get(course_assigned = courses_a)
    if request.method == "POST":
        item = request.POST['name']
        item = float(item)
        if (item > 100):
            item = 100
        elif (item < 0):
            item = 0
        
        t_hold.individual = item
        t_hold.save()
        return redirect("/instructor/threshold/" + str(pk) + "/")

    context = {"pk": pk}
    return render(request, "Program Instructor/CO templates/AddThresholdIndividual.html", context)

def assignoverallthreshold(request, pk):
    courses_a = AssignedCourses.objects.get(id = pk)
    t_hold = Threshold.objects.get(course_assigned = courses_a)
    if request.method == "POST":
        item = request.POST['name']
        item = float(item)
        if (item > 100):
            item = 100
        elif (item < 0):
            item = 0
        t_hold.overall = item
        t_hold.save()
        return redirect("/instructor/threshold/" + str(pk) + "/")

    context = {"pk": pk}
    return render(request, "Program Instructor/CO templates/AddThresholdOverall.html", context)

def assignpothreshold(request, pk):
    courses_a = AssignedCourses.objects.get(id = pk)
    t_hold = Threshold.objects.get(course_assigned = courses_a)
    if request.method == "POST":
        item = request.POST['name']
        item = float(item)
        if (item > 100):
            item = 100
        elif (item < 0):
            item = 0
        t_hold.program = item
        t_hold.save()
        return redirect("/instructor/threshold/" + str(pk) + "/")
    context = {"pk": pk}
    return render(request, "Program Instructor/CO templates/AddThresholdPO.html", context)

def generate_program_outcomes(pk):
    courses_a = AssignedCourses.objects.get(id = pk)
    course = courses_a.course
    created_by = course.created_by
    program = Assign_Program.objects.get(coordinator = created_by)
    program = program.program
    program_outcomes = Program_Outcome.objects.filter(program = program)
    return program_outcomes



def generatetable(request, pk):
    courses_a = AssignedCourses.objects.get(id = pk)
    program_outcomes = generate_program_outcomes(pk)
    print(program_outcomes)


    threshold = Threshold.objects.get(course_assigned = courses_a)
    cos = Course_Outcome.objects.filter(course_assigned = courses_a)
    total_achieved = {}
    for i in range(0, len(cos)):
        temp = cos[i].id
        total_achieved[temp] = 0
    
    students = Student.objects.filter(course_assigned = courses_a)
    list_students = []
    for i in range(len(students)):
        temp = []
        for j in range(len(cos)):
            
            
            result = Result.objects.filter(course_assigned = courses_a, course_outcome = cos[j], student = students[i])
            total = 0
            individual = 0
            for k in range(len(result)):
                individual += result[k].marks_obtained
                total += result[k].totalmarks
            if (total != 0):    
                percentage = (individual/total) * 100
            else:
                percentage = 0
            temp.append(int(percentage))
            if (percentage >= threshold.individual):
                attained = "Y"   
                code = cos[j].id
                total_achieved[code] = 1 
            else:
                attained = "N"
            temp.append(attained)
            
           
        list_students.append({"students": students[i], "maps": temp})
        

    percents = []
    overallatt = []
    no_of_students = []
    co_dict = {}
    for i in range(len(cos)):
        id = cos[i].id
        temp = total_achieved[id]
        no_of_students.append(temp)
        percentage = (temp/len(students) * 100)
        percents.append(int(percentage))
        print(percentage)
        
        if (percentage >= threshold.overall):
            attained = "Y"   
            
            
        else:
            attained = "N"

        co_dict[id] = attained
        
        overallatt.append(attained)
    
    mapping_history = []
    po_total = {}
    po_co_achieved = {}
    for i in range(len(program_outcomes)):
        id = program_outcomes[i].id
        po_total[id] = 0
        po_co_achieved[id] = 0

    for i in range(len(cos)):
        
        id = cos[i].id
        temp = []
        for j in range(len(program_outcomes)):
            pid = program_outcomes[j].id
            map = Mapping.objects.filter(course_outcome = cos[i], program_outcome = program_outcomes[j], course_assigned = courses_a)
            if (len(map) == 0):
                temp.append("")
            elif(co_dict[id] == "Y"):
                temp.append("1")
                po_co_achieved[pid] += 1
                po_total[pid] += 1 
            else:    
                temp.append("0")
                po_total[pid] += 1

        mapping_history.append({"course_outcome": cos[i], "attained":co_dict[id], "temp": temp})  
    print(mapping_history)      
    
    po_percent = []
    po_attained = []
    for i in range(len(program_outcomes)):
        pid = program_outcomes[i].id
        if (po_total[pid] == 0):
            po_percent.append("")
            po_attained.append("")
        else:
            percentage = (po_co_achieved[pid]/po_total[pid] * 100)
            po_percent.append(str(int(percentage)))
            if (percentage >= threshold.program):
                po_attained.append("Y")
            else:
                po_attained.append("N")

    print(po_attained)

    context = {"pk": pk, "course": courses_a, "course_outcomes": cos, "list_students": list_students, "percentages": percents, "attains": overallatt, "numberstudents": no_of_students, "mapping_history": mapping_history, "po_percent": po_percent, "po_attained": po_attained}
    return render(request, "Program Instructor/CO templates/COtable.html", context)

def mark_sheet(request, pk, pk2):
    courses_a = AssignedCourses.objects.get(id = pk)
    questions = Questions.objects.filter(course_assigned = courses_a, type = pk2)
    students = Student.objects.filter(course_assigned = courses_a)
    co = Course_Outcome.objects.filter(course_assigned = courses_a)

    if request.method == "POST":
        print(request.body)
        for i in range(len(questions)):
            id = questions[i].id
            
            item = request.POST[str(id)]

            if (item == "0"):
                questions[i].course_outcome = None
                questions[i].save()
            else:
                co = Course_Outcome.objects.get(id = item)
                questions[i].course_outcome = co
                questions[i].save()

            for j in range(len(students)):
                result = Result.objects.get(question = questions[i], student = students[j])
                result.course_outcome = questions[i].course_outcome
                result.save()

        item = request.POST.getlist("temp")
        print(item)
        for i in range(len(questions)):
            questions[i].totalmarks = item[i]
            questions[i].save()

            for j in range(len(students)):
                result = Result.objects.get(question = questions[i], student = students[j])
                result.totalmarks = questions[i].totalmarks
                result.save()


        k = 0        
        item = request.POST.getlist("Marks")
        for i in range(len(students)):
            for j in range(len(questions)):
                result = Result.objects.get(question = questions[j], student = students[i])
                temp = float(item[k])
                if (temp > result.totalmarks):
                    result.marks_obtained = result.totalmarks
                elif (temp < 0):
                    result.marks_obtained = 0
                else:
                    result.marks_obtained = temp
                result.save()
                k += 1

        return redirect("/instructor/marksheet/" + str(pk) + "/" + str(pk2) + "/")   

    studentes = []
    for i in range(0, len(students)):
        temp = []
        for j in range(0, len(questions)):
            result = Result.objects.get(question = questions[j], student = students[i])
            temp.append(result.marks_obtained)
            
            
        studentes.append({"student": students[i], "temp": temp})
    
    context = {"questions": questions, "studentes": studentes, "co": co, "pk": pk, "pk2": pk2}
    return render(request, "Program Instructor/Marksheet.html" , context)

def newquestion(request, pk, pk2):
    courses_a = AssignedCourses.objects.get(id = pk)
    questions = Questions.objects.filter(course_assigned = courses_a, type = pk2)
    students = Student.objects.filter(course_assigned = courses_a)
    if (len(questions) == 0):
        question = Questions(number = 1, subsection = "a", totalmarks = 0, description="", type=pk2, course_outcome = None, course_assigned = courses_a)
        question.save()
    else:
        next = questions[len(questions) - 1].number + 1
        question = Questions(number = next, subsection = "a", totalmarks = 0, description="", type=pk2, course_outcome = None, course_assigned = courses_a)
        question.save()

    for i in range(len(students)):
        result = Result(totalmarks = question.totalmarks, marks_obtained = 0, question = question, course_assigned = courses_a, course_outcome = None, student = students[i])
        result.save()

    return redirect("/instructor/marksheet/" + str(pk) + "/" + str(pk2) + "/")

def newsubsection(request, pk, pk2):
    courses_a = AssignedCourses.objects.get(id = pk)
    questions = Questions.objects.filter(course_assigned = courses_a, type = pk2)
    students = Student.objects.filter(course_assigned = courses_a)
    if (len(questions) == 0):
         question = Questions(number = 1, subsection = "a", totalmarks = 0, description="", type=pk2, course_outcome = None, course_assigned = courses_a)
         question.save()
    else:
        next = questions[len(questions) - 1]
        num = next.number
        subsection = ord(next.subsection) 
        print(subsection)
        subsection += 1
        temp = chr(subsection)
        question = Questions(number = num, subsection = temp, totalmarks = 0, description="", type=pk2, course_outcome = None, course_assigned = courses_a)
        question.save()

    for i in range(len(students)):
        result = Result(totalmarks = question.totalmarks, marks_obtained = 0, question = question, course_assigned = courses_a, course_outcome = None, student = students[i])
        result.save()

    return redirect("/instructor/marksheet/" + str(pk) + "/" + str(pk2) + "/")    
