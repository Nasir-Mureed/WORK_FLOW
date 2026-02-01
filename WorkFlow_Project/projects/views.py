from django.shortcuts import render ,redirect
from .models import Project
from django.shortcuts import get_object_or_404
from clients.models import *
from django.contrib.auth.decorators import login_required
from sprints.models import Sprint   
from django.db.models import Q
from django.utils.timezone import now
# Create your views here.

@login_required
def addProject(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        title = data.get('title')
        description = data.get('description')
        budget  = data.get('budget')
        paid = data.get('paid')
        startDate = data.get('startDate')
        deadline = data.get('deadline')
        status = bool(data.get('status') == 'on')
        clientId = data.get('client')
        client = None
        if clientId:
            client = Client.objects.get(id = clientId)
        Project.objects.create(
            user = user,
            title = title,
            description =  description,
            budget = budget,
            paid = paid,
            client = client,
            startDate = startDate,
            deadline = deadline,
            status = status,
        )
        return redirect('projects:showProjects')
    clientData = Client.objects.filter(user = request.user)
    return render(request,'projects/addProject.html',{'clients' : clientData})  

@login_required
def editProject(request,id):
    project = get_object_or_404(Project,id=id,user=request.user)
    print(project.id)
    if request.method == 'POST':
        data = request.POST
        project.title = data.get('title')
        project.description = data.get('description')
        project.budget  = data.get('budget')
        project.paid = data.get('paid')
        project.startDate = data.get('startDate')
        project.deadline = data.get('deadline')
        project.status = bool(data.get('status') == 'on')

        project.save()
        
        return redirect('projects:showProjects')
    else:
        print("Not a Post") 
    # compute remaining amount and percent paid safely in the view
        try:
            budget_val = float(project.budget) if project.budget is not None else 0.0
        except (TypeError, ValueError):
            budget_val = 0.0
        try:
            paid_val = float(project.paid) if project.paid is not None else 0.0
        except (TypeError, ValueError):
            paid_val = 0.0

        remaining = max(budget_val - paid_val, 0.0)
        if budget_val > 0:
            percent_paid = int(round(min(max((paid_val / budget_val) * 100.0, 0.0), 100.0)))
        else:
            percent_paid = 0
  
    return render(request,'projects/editProject.html' , {'project':project, 'remaining': remaining, 'percent_paid': f"{percent_paid}%"})  
  
@login_required
def deleteProject(request,id):
    project = Project.objects.filter(id=id,user=request.user)
    if project:
        project.delete()
        return redirect('projects:showProjects')
    return render(request,'projects/showProjects.html')

@login_required
def showProjects(request):
    projects = Project.objects.filter(user=request.user)
    total_budget = sum(project.budget for project in projects)
    active_projects = projects.filter(status=True).count()
    return render(request,'projects/showProjects.html' , { 'projects': projects,'total_budget':total_budget,'active_projects':active_projects } )

@login_required
def searchProject(request):
    if request.method == 'GET':
        data = request.GET
        q = data.get('search')
        projects = Project.objects.filter(Q(user=request.user)& (Q(title__icontains=q) | Q(description__icontains=q)))
    return render(request, 'projects/showProjects.html' , {'projects' : projects , 'q' : q})    

@login_required
def projectDetail(request,id):
    project = Project.objects.get(id=id)
    sprints = Sprint.objects.filter(project=project)
    remainingDays =   (project.deadline - now()).days
    return render(request,'projects/projectDetail.html',{'project':project , 'sprints' : sprints , 'id':id, 'remainingDays':remainingDays})