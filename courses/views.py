from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import *
from django.contrib.auth.models import User


def courses__list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()

    current_user = request.user

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
        # ? courses = Course.objects.all().order_by("-date")

        # *Teacher Way
        # if current_user.is_authenticated:
        #     enrolled_courses = current_user.courses_joined.all()
        #     courses = Course.objects.all().order_by("-date")
        #     for course in enrolled_courses:
        #         courses = courses.exclude(id=course.id)
        # else:
        #     courses = Course.objects.all().order_by('-date')

        # * My Way
        if current_user.is_authenticated:
            courses = Course.objects.exclude(students=current_user)
            # courses = Course.objects.exclude(students__username=current_user)
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
    tags = Tag.objects.all()

    if request.user.is_authenticated:
        enrolled_courses = request.user.courses_joined.all()
    else:
        enrolled_courses = Course.objects.all().order_by("-date")

    context = {
        "course": course,
        "categories": categories,
        "tags": tags,
        "enrolled_courses": enrolled_courses,
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
