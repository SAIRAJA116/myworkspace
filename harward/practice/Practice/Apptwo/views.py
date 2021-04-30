from django.shortcuts import render
from django.http import HttpResponse
from Appone.models import *
# Create your views here.
def index(request):
    return render(request,"Apptwo/index.html",{
        "data" : A.objects.all()
    })