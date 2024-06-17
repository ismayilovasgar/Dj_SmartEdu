from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Teacher


# Create your views here.
class TeacherListView(ListView):
    model = Teacher

    template_name = "teachers.html"
    context_object_name = "teachers"
    # queryset = Teacher.objects.all()[:1]

    # def get_queryset(self):
    #     return Teacher.objects.all()[:2]

    # paginate_by = 2
