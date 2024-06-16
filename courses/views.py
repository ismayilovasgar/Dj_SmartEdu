from django.shortcuts import render
from .models import *


# Create your views here.
def courses__list(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
        "tags": tags,
    }
    return render(request, "courses.html", context)


def course__detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    categories = Category.objects.all()

    context = {
        "course": course,
        "categories": categories,
    }
    return render(request, "course.html", context)


def category__list(request, category_slug):
    courses = Course.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
        "tags": tags,
    }
    return render(request, "courses.html", context)


def tag__list(request, tag_slug):
    courses = Course.objects.filter(tag__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
        "tags": tags,
    }
    return render(request, "courses.html", context)
