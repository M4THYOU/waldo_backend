# forms.py
from django import forms
from .models import *


class WaldoGameForm(forms.ModelForm):
    class Meta:
        model = WaldoGame
        fields = ['img']
