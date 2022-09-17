from django.shortcuts import render,HttpResponse
import requests
from .form import BREEDForm

# Create your views here.
def index(request):
    fn=BREEDForm()
    data={'form':fn}
    return render(request,'print.html',data)
def image(request):
    form=BREEDForm(request.POST)
    if form.is_valid():
        breed= form.cleaned_data['Breed']
        sub_breed= form.cleaned_data['Sub_Breed']
        first = "https://dog.ceo/api/breed/"
        last = "/images/random"
        if(sub_breed=="-"):
            url = first + breed + last
        else:
            url = first + breed + '/' + sub_breed + last
        pic = requests.get(url).json()
    return render(request,'image.html',pic) 

