from django.contrib import admin
from django.urls import path
from courses.views import *

urlpatterns = [
    path("", courses__list, name="courses"),
]
