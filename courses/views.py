from django.shortcuts import render
from .models import *


# Create your views here.
def courses__list(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    context = {
        "courses": courses,
        "categories": categories,
    }
    return render(request, "courses.html", context)


def course__detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    context = {"course": course}
    return render(request, "course.html", context)


def category_detail(request, category_slug):
    courses = Course.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
    }
    return render(request, "courses.html", context)
