from django.urls import path
from django.urls import path, include

from .views import *
from teachers.views import TeacherListView

urlpatterns = [
    # path("", index__page, name="index"),
    path("", IndexView.as_view(), name="index"),
    # path("about/", about__page, name="about"),
    path("about/", AboutView.as_view(), name="about"),
    # path("courses/", courses__page, name="courses"),
    path("teachers/", include("teachers.urls")),
    # path("teachers/", TeacherListView.as_view(), name="teacher-list"),
    path("contact/", ContactView.as_view(), name="contact"),
    # *
    # *
    # *
    # *path(route,view,op(kisayol ismi))
]
