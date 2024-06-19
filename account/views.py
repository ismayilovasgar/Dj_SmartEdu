from django.shortcuts import render


# Create your views here.
def user__login(request):
    return render(request, "login.html")


def user__register(request):
    return render(request, "register.html")


def user__dashboard(request):
    pass


def user__logout(request):
    pass
