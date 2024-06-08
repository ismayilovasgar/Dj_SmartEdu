from django.urls import path
from .views import *

urlpatterns = [
    path("", index__page, name="index"),
    path("about/", about__page, name="about"),
    path("courses/", courses__page, name="courses"),
    path("teachers/", teachers__page, name="teachers"),
    path("contact/", contact__page, name="contact"),
]
