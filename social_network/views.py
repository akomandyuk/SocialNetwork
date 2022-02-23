from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Profile, CreateTeam
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'socnet/homepage.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'socnet/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'socnet/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has been taken. Please create another one'})
        else:
            return render(request, 'socnet/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords didn\'t match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'socnet/loginuser.html', {'form': AuthenticationForm()})
    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if user is None:
           return render(request, 'socnet/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username or Password didn\'t match'})
       else:
           login(request, user)
           return redirect('dashboard')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')

@login_required
def createteams(request):
    if request.method == 'GET':
        return render(request, 'socnet/createteams.html', {'form': CreateTeam()})
    else:
        try:
            form = CreateTeam(request.POST)
            new_team = form.save(commit=False)
            new_team.user = request.user
            new_team.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'socnet/createteams.html', {'form': CreateTeam(), 'error': 'Bad data passed in. Try again'})

@login_required
def dashboard(request):
    teams = CreateTeam.objects.all()
    return render(request, 'socnet/dashboard.html', {'teams': teams})


@login_required
def userprofile(request, username):
    profile = Profile.objects.get(username=username)
    return render(request, 'socnet/userprofile.html', {"profile": profile})



@login_required
def teamprofile(request, username):
    team = CreateTeam.objects.get(username=username)
    return render(request, 'socnet/userprofile.html', {"team": team})