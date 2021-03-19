from django import forms
from .models import *


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
