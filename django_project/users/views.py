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
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        # form = UserCreationForm() # built in form of django
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

print(f"Current Crispy Pack: {settings.CRISPY_TEMPLATE_PACK}")