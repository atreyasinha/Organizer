from django.forms import ModelForm
from django import forms

from .models import *

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['description', 'category', 'projected', 'actual']
