from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('' ,views.showProjects, name='showProjects' ),
    path('add/' , views.addProject , name = 'addProject'),
    path('search/' , views.searchProject , name = 'searchProject'),
    path('edit/<int:id>/' , views.editProject , name = 'editProject'),
    path('delete/<int:id>/' , views.deleteProject , name = 'deleteProject'),
    path('detail/<int:id>/' , views.projectDetail , name = 'projectDetail'),

]