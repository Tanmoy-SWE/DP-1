from doctest import FAIL_FAST
from pickle import TRUE
from django.shortcuts import render, redirect

from Authentication.models import User
from InstitutionAdmin.models import All_Coordinators
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def adminauth(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)           
            uobj.save()
            return redirect('adminlogin')
    context = {'form': form }
    return render(request, 'AdminRegistrationPage.html', context)

def coordinatorauth(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)    
            uobj.is_admin = False
            uobj.is_coordinator = True
            uobj.save()
            
            coords = All_Coordinators(coordinator = uobj, isAssigned = False)
            coords.save()
        
            
            return redirect('coordinatorlogin')
    context = {'form': form }
    return render(request, 'ProgramCoordinatorRegistrationPage.html', context)

def instructorauth(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)    
            uobj.is_admin = False
            uobj.is_instructor = True
            uobj.save()
            return redirect('instructorlogin')
    context = {'form': form }
    return render(request, 'ProgramInstructorRegistrationPage.html', context)

def adminlogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_admin) == 1:
                login(request, user)
                return redirect('/institutionAdmin/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'AdminLoginPage.html', context)

def coordinatorlogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_coordinator) == 1:
                login(request, user)
                return redirect('/coordinator/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'ProgramCoordinatorLoginPage.html', context)

def instructorlogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_instructor == 1):
                login(request, user)
                return redirect('/instructor/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'ProgramInstructorLoginPage.html', context)

def home(request):
    return render(request , 'LoginPage.html')
