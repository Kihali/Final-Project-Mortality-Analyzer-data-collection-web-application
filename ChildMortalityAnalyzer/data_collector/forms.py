from django import forms
from .models import ChildMortality

class ChildMortalityForm(forms.ModelForm):
    class Meta:
        model = ChildMortality
        fields = ['year', 'mortality_rate']
