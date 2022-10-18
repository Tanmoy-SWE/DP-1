from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login(request):
    return render(request , 'ProgramCoordinatorLoginPage.html')

def registration(request):
    return render(request , 'ProgramCoordinatorRegistrationPage.html')

def coordinatorHome(request):
    return render(request, 'Program Coordinator/CoordinatorHome.html')

def logout_user(request):
    logout(request)
    return redirect('/')
