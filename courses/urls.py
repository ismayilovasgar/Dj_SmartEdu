from django.contrib import admin
from django.urls import path
from courses.views import courses__list, course__detail, category_detail

urlpatterns = [
    path("", courses__list, name="courses"),
    path("<slug:category_slug>/<int:course_id>", course__detail, name="course_detail"),
    path("categories/<slug:category_slug>", category_detail, name="courses_by_category"),
]
