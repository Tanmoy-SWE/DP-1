from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request , 'Home.html')

def cour_ins_form(request):
    return render(request , 'CourseInstructorForm.html')
