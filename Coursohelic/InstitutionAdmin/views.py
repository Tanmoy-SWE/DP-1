from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ProgramForm
from .models import Program
from Authentication.models import User



# Create your views here.


def home(request):
    return render(request , 'AdminHome.html')

def coordinator_list(request):
    return render(request, 'ProgramCoordinatorList.html')

def program_list(request):
    list_of_programs = Program.objects.filter(created_by=request.user)
    return render(request, 'ProgramList.html', {'programs': list_of_programs})

def delete_program(request, pk):
    program = Program.objects.get(p_id=pk)
    program.delete()
    return redirect('/institutionAdmin/ProgramList/')


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

def addCoordinator(request):
    coordinator = User.objects.filter(is_coordinator = True, institution = request.user.institution)
    print(coordinator)
    print(request.user.first_name)
    context = {'coordinator' : coordinator}
    return render(request, 'AvailableCoordinatorList.html', context)

def assignCoordinator(request, pk):
    programs = Program.objects.filter(created_by = request.user)
    coordinator = User.objects.get(id = pk)
    print(coordinator.institution)
    context = {'programs' : programs , 'coordinator' : coordinator}
    return render(request, 'AddCoordinator.html', context)