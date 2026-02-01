from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard , name = 'dashboard'),
    path('about/', views.about , name = 'about'),
    path('contact/', views.contact , name = 'contact'),
    path('profile/', views.myProfile , name = 'profile'),
    path('help/', views.help , name = 'help'),
]