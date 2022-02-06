from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Data
from .forms import MyForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "dashboard/dashboard.html",{
        "datas": Data.objects.all()
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "dashboard/login.html", {
                "message": "Invalid Credentials! Login again."
            })
    return render(request, "dashboard/login.html")

def logout_view(request):
    logout(request)
    return render(request, "dashboard/login.html", {
        "message": "Logged out."
    })

def update(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = MyForm()
    return render(request, "dashboard/update.html", {
        "form": form
    })



