from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import *


# Create your views here.


def courses__list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if category_slug != None:
        # courses = get_list_or_404(Course, available=True, category__slug=category_slug)

        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(available=True, category=category_page)

        # courses = Course.objects.filter(available=True, category__slug=category_slug)

    elif tag_slug != None:
        # courses = get_list_or_404(Course, available=True, tag__slug=tag_slug)

        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(available=True, tag=tag_page)

        # courses = Course.objects.filter(available=True, tag__slug=tag_slug)

    else:
        courses = Course.objects.all().order_by("-date")

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


def search(request):
    courses = Course.objects.filter(name__contains=request.POST["search-k"])
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "categories": categories,
        "tags": tags,
        "courses": courses,
    }
    return render(request, "courses.html", context)





# def category__list(request, category_slug):
#     courses = Course.objects.filter(category__slug=category_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         "courses": courses,
#         "categories": categories,
#         "tags": tags,
#     }
#     return render(request, "courses.html", context)


# def tag__list(request, tag_slug):
#     courses = Course.objects.filter(tag__slug=tag_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()


#     context = {
#         "courses": courses,
#         "categories": categories,
#         "tags": tags,
#     }
#     return render(request, "courses.html", context)


# def courses__list(request):
#     courses = Course.objects.all()
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         "courses": courses,
#         "categories": categories,
#         "tags": tags,
#     }
#     return render(request, "courses.html", context)
