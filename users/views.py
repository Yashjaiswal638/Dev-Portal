from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles' : profiles
    }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        'profile':profile,
        'topSkills':topSkills,
        'otherSkills':otherSkills,
    }
    return render(request, 'users/user-profile.html', context)


def loginUser(request):
    page = "login"
    context = {'page':page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try :
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist!!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            # sends the session to the browser
            return redirect('profiles')
        else :
            messages.error(request, "Username OR Password is incorrect")

    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.error(request, "User is logged out!!")
    return redirect('login')


def registerUser(request):
    page = "register"
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=false)
            user.username = user.username.lower()
            user.save()

    context = {
        'page':page,
        'form':form,
    }
    return render(request, 'users/login_register.html', context)