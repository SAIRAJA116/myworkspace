from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import UserForm
from .decorators import unauthenticated_user
# Create your views here.



@unauthenticated_user
def  registerpage(request):
    form=  UserForm()
    if request.method=="POST":
        form = UserForm(request.POST)
        if(form.is_valid()):
            form.save()

            messages.success(request,"account successfully created for "+form.cleaned_data.get('username'))
            return redirect("login")

    return render(request,"Todo/register.html",{"form":form})

@unauthenticated_user
def loginpage(request):
    if (request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            
            return redirect("home")
        else:
            messages.info(request,"username or password is incorrect")
    
    return render(request,"Todo/login.html")
 

@login_required(login_url='login')
def home(request):
    task = Task.objects.all()
    return render(request,"Todo/index.html",{"task":task})


def adminpannel(request):
    if (request.user.is_authenticated== True):
        return HttpResponseRedirect("admin")
    else:
        return redirect("login")


@login_required(login_url='login')
def addTask(request):
    if(request.method=='POST'):
        o=Task(task=request.POST.get('task'))
        o.save()
        return HttpResponseRedirect(reverse("home"))


@login_required(login_url='login')
def delete(request,id):
    Task.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("home"))


@login_required(login_url='login')
def logoutpage(request): 
    logout(request)
    return redirect("login")

