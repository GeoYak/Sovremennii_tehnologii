from django import forms
from .models import ServiceModel


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = "__all__"
