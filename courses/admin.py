from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "available",
    )
    list_filter = ("available",)
    search_fields = (
        "name",
        "description",
    )
