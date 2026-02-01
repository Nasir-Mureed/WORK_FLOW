from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('',views.signup,name='signup'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logout,name='logout'),
]