from django.shortcuts import render


# Create your views here.
def index__page(request):
    return render(request, "index.html")


def about__page(request):
    return render(request, "about.html")


# def courses__page(request):
#     return render(request, "courses.html")


def teachers__page(request):
    return render(request, "teachers.html")


def contact__page(request):
    return render(request, "contact.html")
