from django.db import models
from django.urls import reverse
from teachers.models import Teacher
from django.contrib.auth.models import User


# Create your models here.
# * manyToMany
class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


# * oneToMany or manyToOne
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Kurs Adi",
        help_text="Kurs Adini Yaziniz",
    )

    # *  Realtionships
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(
        User, blank=True, null=True, related_name="courses_joined"
    )
    # *  ************

    description = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(
        upload_to="courses/%Y/%m/%d/", default="default_course_image.png"
    )
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
