from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def auth(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form }
    return render(request, 'AdminRegistrationPage.html', context)

def login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('AdminHome')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'AdminLoginPage.html', context)
    
def home(request):
    return render(request , 'AdminHome.html')
