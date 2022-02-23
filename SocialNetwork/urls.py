"""Project_TMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from social_network import views
from social_network.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

#Auth

    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

#SocNet
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('createteams/', views.createteams, name='createteams'),
    #path('userprofile/<int:pk>/', views.userprofile, name='userprofile'),
    path('socnet/<int:team_pk>', views.teamprofile, name='teamprofile'),
    #path('createprofile/', views.createprofile, name='createprofile'),
    #path('editprofile/', views.editprofile, name='editprofile_page'),
]
