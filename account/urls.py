from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login/", user__login, name="login"),
    path("register/", user__register, name="register"),
    path("dashboard/", user__dashboard, name="dashboard"),
    path("logout/", user__logout, name="logout"),
]
