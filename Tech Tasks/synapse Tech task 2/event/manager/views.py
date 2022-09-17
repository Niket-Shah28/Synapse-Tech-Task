from django.shortcuts import render,HttpResponseRedirect
from .form import Manage
from .models import Event

# Create your views here.
def index(request):
    if request.method=="POST":
        fm=Manage(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Manage()
    else:
        fm=Manage()
    eve=Event.objects.all()
    return render(request,'block.html',{'form':fm,'eve':eve})
#This deletes data
def delete_data(request,id):
    if request.method=="POST":
        pi=Event.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
#This one updates the data
def update_data(request,id):
    if request.method=="POST":
        pi=Event.objects.get(pk=id)
        fm=Manage(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Event.objects.get(pk=id)
        fm=Manage(instance=pi)
    return render(request,'update.html',{'form':fm})