from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from .models import Profile
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User






def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
        try:
            Profile.create_user_and_send_credentials_via_email(full_name=full_name, email=email)
           
            return HttpResponse('Check email for credentials')

        except IntegrityError as e:
            return HttpResponse(e)
        else:
            return HttpResponse('Invalid form')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



# login user
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['user']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Successfully login')
            else:
                return HttpResponse("User does not exist")

        return HttpResponse("Invalid credentials")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})
