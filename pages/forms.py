from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "First NameXXX",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Last NameXXX",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "EmailXXX",
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "PhoneXXX",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "MessageXXX",
            }
        )
    )

    class Meta:
        model = Contact
        # fields = "__all__"
        fields = ["first_name", "last_name", "email", "phone", "message"]
