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
        
        print(project.title)

        Sprint.objects.create(
            name = name,
            startDate=startDate,
            endDate =endDate,
            project=project,
        )
        return redirect("projects:projectDetail",id)
    return render(request,'sprints/createSprint.html' , {'today' : now ,'id':id })