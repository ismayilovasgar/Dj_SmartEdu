from django.contrib import admin
from django.urls import path
from courses.views import courses__list, course__detail

urlpatterns = [
    path('', courses__list, name="courses"),
    path("<slug:category_slug>/<int:course_id>", course__detail, name="course_detail"),
]
