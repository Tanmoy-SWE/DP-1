from django.shortcuts import render
from .forms import CreateUserForm

# Create your views here.
def auth(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form }
    print(form['institution'])
    return render(request, 'AdminRegistrationPage.html', context)
