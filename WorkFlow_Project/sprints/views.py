from django.shortcuts import render,redirect
from .models import *
from django.utils.timezone import now
from projects.models import Project
from .models import Sprint
# Create your views here.

def createSprint(request,id):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        startDate = data.get('startDate')
        endDate = data.get('endDate')  
        project  = Project.objects.get(id=id)
        isActive =bool(data.get('status')=="on")
        
        print(project.title)

        Sprint.objects.create(
            name = name,
            startDate=startDate,
            endDate =endDate,
            project=project,
            isActive = isActive,
        )
        return redirect("projects:projectDetail",id)
    return render(request,'sprints/createSprint.html' , {'today' : now ,'id':id })

def editSprint(request,projectId,sprintId):
    sprint = Sprint.objects.get(id=sprintId)
    if request.method == 'POST':
        data = request.POST
        sprint.name = data.get('name')
        sprint.startDate = data.get('startDate')
        sprint.endDate = data.get('endDate')  
        sprint.isActive =bool(data.get('status')=="on")
        sprint.save()
        return redirect("projects:projectDetail",projectId)
    return render(request,'sprints/editSprint.html' , {'id':projectId ,'sprint':sprint })