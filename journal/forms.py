from django.forms import ModelForm
from django import forms

from .models import *

class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ['description', 'entry']
