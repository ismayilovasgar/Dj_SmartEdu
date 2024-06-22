from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from courses.models import Course


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


@login_required(login_url="login")
def user__dashboard(request):
    current_user = request.user
    courses = current_user.courses_joined.all()
    context = {"courses": courses}

    return render(request, "dashboard.html", context)


@login_required(login_url="login")
def user__logout(request):
    logout(request)
    return redirect("index")


@login_required(login_url="login")
def enroll_the_course(request):
    course_id = request.POST["course_id"]
    user_id = request.POST["user_id"]

    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=user_id)
    course.students.add(user)
    return redirect("dashboard")
