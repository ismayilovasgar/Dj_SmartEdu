from django.contrib import admin
from .models import Teacher


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "title")
    search_fields = ("name", "description")
