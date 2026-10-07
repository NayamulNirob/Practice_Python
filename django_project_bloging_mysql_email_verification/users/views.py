from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from .models import PendingUser

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile


# Create your views here.


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # built in form of django
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # 1. Get the data from the form
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            # 2. Hash the password manually exactly ONCE
            # We use make_password here and will use .create() in verify_account
            # hashed_password = make_password(password)

            # 3. Save to the PendingUser model instead of User
            pending_user = PendingUser.objects.create(
                username=username,
                email=email,
                password=password
            )

            # 4. Create the verification link using the token
            verification_link = f"http://127.0.0.1:8000/verify/{pending_user.token}/"

            send_mail(
                'Verify your account',
                f'Welcome! please click this link to create your account: {verification_link}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            messages.success(request,
                             f'Registration request sent! Please check your email to complete your account creation.')
            return redirect('login')
    else:
        # form = UserCreationForm() # built in form of django
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def verify_account(request, token):
    try:
        with transaction.atomic():
            # 1. Find the pending user
            pending_user = PendingUser.objects.get(token=token)

            # 2. Create the actual user using create_user (handles hashing)
            user = User.objects.create_user(
                username=pending_user.username,
                email=pending_user.email,
                password=pending_user.password
            )

            # 3. Create the associated profile
            Profile.objects.get_or_create(user=user)

            # 4. CRITICAL: Delete the pending record so they are no longer "Pending"
            pending_user.delete()

        messages.success(request, 'Your account has been verified and created! You can now login.')
        return redirect('login')
    except PendingUser.DoesNotExist:
        messages.error(request, 'Invalid or expired verification link.')
        return redirect('register')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('register')





def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required(login_url='/login/')  # this is optional we can set this login_url at setting.py as LOGIN_URL = 'login'
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
