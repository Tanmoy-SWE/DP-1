from django.shortcuts import render

# Create your views here.
def cour_ins_form(request):
    return render(request , 'CourseInstructorForm.html')
