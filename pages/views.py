from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# *Function base template view
# def index__page(request):
#     return render(request, "index.html")


# def about__page(request):
#     return render(request, "about.html")


# def teachers__page(request):
#     return render(request, "teacher.html")


def contact__page(request):
    return render(request, "contact.html")


# *Class based template view
class AboutView(TemplateView):
    template_name = "about.html"


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(available=True).order_by("-date")[:2]
        context["total_course"] = Course.objects.filter(available=True).count()
        return context


class ContactView(SuccessMessageMixin, FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")
    success_message = "We received your messages."

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
