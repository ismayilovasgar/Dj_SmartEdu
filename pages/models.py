from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.first_name}"
