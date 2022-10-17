from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def adminauth(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminlogin')
    context = {'form': form }
    return render(request, 'AdminRegistrationPage.html', context)

def adminlogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_admin == 1):
                login(request, user)
                return redirect('/institutionAdmin/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'AdminLoginPage.html', context)

    
def home(request):
    return render(request , 'LoginPage.html')
