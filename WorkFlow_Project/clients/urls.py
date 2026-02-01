from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('',views.clients,name='clients'),
    path('edit/<int:id>/',views.editClient,name='editClient'),
    path('delete/<int:id>/',views.deleteClient,name='deleteClient'),
    path('add',views.addClient,name='addClient'),
]