from django.urls import path
from . import views

app_name = 'userStories'

urlpatterns = [
    path('userStories/<int:id>/',views.displayUserStories,name='displayUserStories'),
    path('create/<int:id>/',views.createStory,name='createStory'),
    path('delete/<int:id>/',views.deleteStory,name='deleteStory'),
]
