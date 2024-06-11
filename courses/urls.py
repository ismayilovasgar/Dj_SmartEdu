from django.contrib import admin
from django.urls import path
from courses.views import courses__list

urlpatterns = [
    path("/", courses__list, name="courses"),
]
