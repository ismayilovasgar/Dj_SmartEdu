from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Contact)
class ContatcAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email", "message"]

    class Meta:
        model = Contact
