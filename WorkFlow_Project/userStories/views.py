from django.shortcuts import render,redirect
from userStories.models import UserStory
from sprints.models import Sprint

# Create your views here.

def displayUserStories(request,id): # id of Sprint
   
    sprint=Sprint.objects.get(id=id)
    userStories=UserStory.objects.filter(sprint=sprint)
    return render(request,'userStories/displayUserStories.html' , {'userStories':userStories , 'sprint':sprint})

def createStory(request,id):
    if request.method=='POST':
        data=request.POST
        descrip=data.get('description')
        sprint =Sprint.objects.get(id=id)

        UserStory.objects.create(
            description=descrip,
            sprint=sprint
        )

        return redirect('userStories:displayUserStories',id)
    return render(request,'userStories/createStory.html',{'id':id})

def deleteStory(request,id):
    story=UserStory.objects.get(id=id)
    sprintId=story.sprint.id
    story.delete()
    return redirect('userStories:displayUserStories',sprintId)