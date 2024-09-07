from django import forms
from .models import ChildMortality

class ChildMortalityForm(forms.ModelForm):
    class Meta:
        model = ChildMortality
        fields = [
            'facility_name', 'facility_location', 'facility_capacity', 
            'child_age', 'child_gender', 'cause_of_death', 
            'region_name', 'population', 'gdp'
        ]
