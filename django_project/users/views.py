from django.contrib.auth import logout
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.conf import settings
# Create your views here.


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # built in form of django
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}! You can now login')
            return redirect('login')
    else:
        # form = UserCreationForm() # built in form of django
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html',)