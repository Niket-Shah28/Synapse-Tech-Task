from django.core import validators
from django import forms 
from .models import Event

class Manage(forms.ModelForm):
    class Meta:
        model=Event
        fields=['Event_Name','Start_Date','End_Date','No_of_People','Situation']