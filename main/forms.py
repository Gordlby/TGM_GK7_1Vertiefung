from django import forms
from .models import Fach

class FachForm(forms.ModelForm):
    class Meta:
        model = Fach
        fields = ['name', 'description']

