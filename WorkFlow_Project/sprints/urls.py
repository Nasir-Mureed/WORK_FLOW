from django.urls import path
from . import views

app_name = 'sprints'

urlpatterns = [
     path('create/<int:id>/',views.createSprint,name='createSprint')
]
