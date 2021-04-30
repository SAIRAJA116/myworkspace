from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewForm(forms.Form):
    task = forms.CharField(label="NewTask")
    priority = forms.IntegerField(label="priority" , max_value=8, min_value=1)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"todo/index.html",{
        "tasks" : request.session["tasks"]
    })

def add(request):
    if(request.method=="POST"):
        form = NewForm(request.POST)
        if(form.is_valid()==True):
            task= form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"todo/add.html",{
                "form" : form
            })
    return render(request, "todo/add.html",{
        "form" : NewForm()
    })