from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Create your views here.
def signup(request):
    if request.method == 'POST':
        data = request.POST
        firstName = data.get('first-name')
        lastName = data.get('last-name')
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username is already taken. try another")
            return redirect('accounts:signup')
        else: 
            user = User.objects.create_user(
                username=username,
                password=password
            )

            Profile.objects.create(
                user = user,
                firstName =firstName,
                lastName = lastName
            )
            messages.success(request , "Registered Successfully!")
            return redirect('accounts:login')
    return render(request, 'accounts/signup.html')

def loginUser(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request,username = username,password=password)
        
        if user:
            login(request,user)
            messages.success(request ,"Login Successfully")
            return redirect("dashboard:dashboard")
        else:
            messages.error(request , "Invalid Username or Password")
            redirect('accounts:login')
    return render(request, 'accounts/login.html')

def logout(request):
    logout(request)
    return render(request, 'accounts/logout.html')

