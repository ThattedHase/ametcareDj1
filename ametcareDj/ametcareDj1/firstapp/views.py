
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .forms import UserInfo
from .forms import PreferencesForm



def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0} {1} {2}</h2>".format(name,email,password))
    else:
        userform = UserForm()
        return render(request, "register.html", {"form": userform})



def userinfo(request):
    if request.method == "POST":
        gender = request.POST.get("gender")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        age = request.POST.get("age")
        task = request.POST.get("task")
        return HttpResponse("<h2>Hello, {0} {1} {2}</h2>".format(gender, weight, height))
    else:
        form = UserInfo()
        return render(request, "userinfo.html", {"form": form})

def indpref(request):
    if request.method == "POST":
        pref = request.POST.getlist("preferences")
        return HttpResponse("<h2>Hello, {0}</h2>".format(pref))
    else:
        form = PreferencesForm()
        return render(request, "indpref.html", {"form": form})


def start1(request):
    return render(request, "start1.html")

def start2(request):
    return render(request, "start2.html")

def login(request):
    return render(request, "login.html")

def choose(request):
    return render(request, "choose.html")

def allergy(request):
    return render(request, "allergy.html")

