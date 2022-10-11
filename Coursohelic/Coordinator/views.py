from django.shortcuts import render, redirect

# Create your views here.

def coordinator(request):
    return render(request , 'CoordinatorForm.html')