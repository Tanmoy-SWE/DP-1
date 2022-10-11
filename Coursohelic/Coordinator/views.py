from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request , 'ProgramCoordinatorLoginPage.html')

def registration(request):
    return render(request , 'ProgramCoordinatorRegistrationPage.html')
