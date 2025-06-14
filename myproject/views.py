from .forms import RegistrationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login

def register_user(request):
    if (request.method == "POST"):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user) #login the user automatically
            return redirect('feeds_list')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {"form" : form})