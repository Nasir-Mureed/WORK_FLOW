from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from projects.models import Project
from clients.models import Client
from accounts.models import Profile
from .models import Contact
# Create your views here.

def home(request):
    return render(request , 'dashboard/home.html')

@login_required
def dashboard(request):
    projectCount = Project.objects.filter(user = request.user).count()
    clientCount = Client.objects.filter(user = request.user).count()
    projects = Project.objects.filter(user = request.user)
    totalAmount = 0
    totalPaid = 0
    for p in projects:
        totalAmount = totalAmount + p.budget
        totalPaid=totalPaid + p.paid
    remainingAmount = totalAmount - totalPaid
    context = {
        'username' : request.user,
        'projectCount' : projectCount,
        'clientCount' : clientCount,
        'totalAmount':totalAmount,
        'totalPaid':totalPaid,
        'remainingAmount' : remainingAmount,
    }
    return render(request , 'dashboard/dashboard.html', context=context)

def about(request):
    return render(request , 'dashboard/about.html')
    
@login_required    
def myProfile(request):
    profile = Profile.objects.get(user = request.user)
    print(profile)
    return render(request,'dashboard/myprofile.html' , {'profile' : profile})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return redirect('dashboard:home')

    return render(request , 'dashboard/contact.html')

def help(request):
    return render(request , 'dashboard/help.html')