from django.shortcuts import render
from .models import Course


# Create your views here.
def courses__list(request):
    courses = Course.objects.all().order_by("-date")
    context = {"courses": courses}
    return render(request, "courses.html", context)
