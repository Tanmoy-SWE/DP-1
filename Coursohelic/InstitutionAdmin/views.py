from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ProgramForm



# Create your views here.


def home(request):
    return render(request , 'AdminHome.html')

def coordinator_list(request):
    return render(request, 'ProgramCoordinatorList.html')

def program_list(request):
    return render(request, 'ProgramList.html')

def add_program(request):
    form = ProgramForm()
    context = {'form': form}
    
    

def logout_user(request):
    logout(request)
    return redirect('/')