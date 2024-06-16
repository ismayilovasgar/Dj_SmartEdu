from django.contrib import admin
from django.urls import path
from courses.views import *

urlpatterns = [
    path("", courses__list, name="courses"),
    path("<slug:category_slug>/<int:course_id>", course__detail, name="course_detail"),
    path("categories/<slug:category_slug>", category__list, name="courses_by_category"),
    path("tags/<slug:tag_slug>", tag__list, name="courses_by_tag"),
]
