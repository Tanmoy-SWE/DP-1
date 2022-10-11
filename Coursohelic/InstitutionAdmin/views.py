from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request , 'AdminLoginPage.html')

def registration(request):
    return render(request , 'AdminRegistrationPage.html')