from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
    return HttpResponse("hello world!")

def name(request,n):
    return HttpResponse("Hello "+n)

def new(request):
    return render(request,"App/new.html")

def greet(request,name):
    return render(request,"App/greet.html",{"data" : name})

def practice(request):
    l={"raja","keerthi","swamy","sandy"}
    return render(request,"App/practice.html",
    {
        "data": l
    }
    )