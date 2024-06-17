from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=250)
    image = models.ImageField(
        upload_to="courses/%Y/%m/%d/", default="default_course_image.png"
    )
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.title}"
