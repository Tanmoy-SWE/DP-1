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



# todo_list/todo_app/views.py
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic import ListView
from .models import ToDoList, ToDoItem

class ListListView(ListView):
    model = ToDoList
    template_name = "accreditation.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("accreditation")

class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context