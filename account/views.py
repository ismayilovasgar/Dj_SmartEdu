from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def user__login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    messages.info(request, "Disabled Account !")

            else:
                messages.info(request, "Check Username or Password !")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def user__register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created, You can Login !")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def user__dashboard(request):
    pass


def user__logout(request):
    pass
