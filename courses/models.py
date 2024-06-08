from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):

    name = models.CharField(max_length=50,unique=True,verbose_name="Kurs Adi",help_text="Kurs Adini Yaziniz")
    description = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_course_image.jpg")
    date=models.DateTimeField(auto_now=True)
    avaialable=models.BooleanField(default=True)

    
    def __str__(self):
        return f"{self.name} | {self.date}"

