from django import forms
from .models import CheckIn

class checkin_form(forms.ModelForm):
    checkin_form = forms.Model