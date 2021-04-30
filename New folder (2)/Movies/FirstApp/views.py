from django.shortcuts import render
from .forms import MovieForm
from django.http import HttpResponse
from .models import Movie
from django.contrib import messages
# Create your views here.
def register(request):
	form = MovieForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		data=Movie.objects.get(moviename = request.POST['moviename'])
		data.director = 'raja'
		data.save()
		#messages.success(request,request.POST['moviename'] + ' '+data.director+'is added successfully')
		return HttpResponse('Done')

	form = MovieForm()
	return render(request,'register.html',{'myform':form})


def showall(request):
	data=Movie.objects.all()

	return render(request,'showall.html',{'data':data})