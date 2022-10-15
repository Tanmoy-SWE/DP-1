from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request , 'AdminHome.html')

def CoordinatorList(request):
    return render(request, 'ProgramCoordinatorList.html')

def ProgramList(request):
    return render(request, 'ProgramList.html')