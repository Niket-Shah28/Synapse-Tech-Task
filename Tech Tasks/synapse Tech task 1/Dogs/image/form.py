from socket import fromshare
from django import forms 
from django.urls import path
from . import views

class BREEDForm(forms.Form):
    Breed=forms.CharField()
    Sub_Breed=forms.CharField()
