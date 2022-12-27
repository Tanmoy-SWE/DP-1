from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ProgramForm
from .models import All_Coordinators, Assign_Program, Program
from Coordinator.models import Program_Outcome
from Authentication.models import User



# Create your views here.


def home(request):
    return render(request , 'AdminHome.html')

def coordinator_list(request):
    coordinator = All_Coordinators.objects.filter(isAssigned=True)
    coordinators = []
    for i in range(0, len(coordinator)):
        if (coordinator[i].coordinator.institution == request.user.institution):
            coordinators.append(coordinator[i].coordinator)
    
    program = []
    for i in range(0, len(coordinators)):
        temp = Assign_Program.objects.get(coordinator = coordinators[i])
        program.append(temp)
        a = 5

    print(coordinators)
    context = {'programs': program}
    return render(request, 'ProgramCoordinatorList.html', context)

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

        for i in range(0,12):
            po_number = "PO" + str(i+1)
            new_po = Program_Outcome(c_code = po_number, program = new_program)
            new_po.save()
            
        return redirect('/institutionAdmin/ProgramList/')

    return render(request, 'AddProgram.html')
    
    


def logout_user(request):
    logout(request)
    return redirect('/')

def addCoordinator(request):
    #coordinator = User.objects.filter(is_coordinator = True, institution = request.user.institution)
    coordinator = All_Coordinators.objects.filter(isAssigned=False)
    print(coordinator)
    coordinators = []
    for i in range(0, len(coordinator)):
        if (coordinator[i].coordinator.institution == request.user.institution):
            coordinators.append(coordinator[i].coordinator)
    print(coordinators)
    print(request.user.first_name)
    context = {'coordinator' : coordinators}
    return render(request, 'AvailableCoordinatorList.html', context)

def deassign_coordinator(request, pk):
    coordinator1 = Assign_Program.objects.get(id = pk)
    coordinator_info = coordinator1.coordinator 
    coordinator_object = All_Coordinators.objects.get(coordinator = coordinator_info)
    coordinator_object.isAssigned = False
    coordinator_object.save()
    coordinator1.delete()
    return redirect('/institutionAdmin/ProgramCoordinatorList/')

def coordinator_confirmation(request, pk):

    context = {'pk' : pk}
    return render(request, 'DeleteConfirmation.html', context)

def go_back(request):
    return redirect('ProgramCoordinatorList/')

def go_back_program(request):
    return redirect('ProgramList/')


    


def assignCoordinator(request, pk):
    programs = Program.objects.filter(created_by = request.user)
    coordinator = User.objects.get(id = pk)
    if request.method == "POST":
        pro_name = request.POST['choice']
        program = Program.objects.get(p_name = pro_name, created_by = request.user)
        coord = Assign_Program(coordinator = coordinator, program = program)
        coord.save()

        temp = All_Coordinators.objects.get(coordinator = coordinator)
        temp.isAssigned = True
        temp.save()

        return redirect("/institutionAdmin/ProgramCoordinatorList/")



    context = {'programs' : programs , 'coordinator' : coordinator}
    return render(request, 'AddCoordinator.html', context)


def program_confirmation(request, pk):
    
    context = {'pk' : pk}
    return render(request, 'DeleteConfirmationProgram.html', context)