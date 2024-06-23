from django.contrib import admin
from .models import Course, Category, Tag


# Register your models here.
# * oneToMany or manyToOne
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "available", "teacher")
    list_filter = ("available",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# * manyToMany
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
