from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ProgramForm
from .models import Program



# Create your views here.


def home(request):
    return render(request , 'AdminHome.html')

def coordinator_list(request):
    return render(request, 'ProgramCoordinatorList.html')

def program_list(request):
    return render(request, 'ProgramList.html')

def add_program(request):
    
    if request.method == 'POST':
        user = request.user
        print(user)
        name = request.POST['program']
        department = request.POST['department']
        description = request.POST['message']
        total_credit = request.POST['total_credit']

        new_program = Program(p_name = name, department = department, description = description, total_credit = total_credit, created_by = user)
        new_program.save()
        return redirect('/institutionAdmin/ProgramList/')

    return render(request, 'AddProgram.html')
    
    
    

def logout_user(request):
    logout(request)
    return redirect('/')