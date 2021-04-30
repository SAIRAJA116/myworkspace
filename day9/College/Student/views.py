from django.shortcuts import render,redirect
from .models import student
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'Student/home.html')

def register(request):
	if request.method == 'POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		email=request.POST.get('email')
		Age=request.POST.get('age')
		branch = request.POST.get('branch')
		

		#return render(request,'Student/data.html',{'fname':fname,'lname':lname,'branch':branch,'email':email,'gender':gender})
		obj = student(First_name = fname,Last_name=lname,branch=branch,Age=Age,Email=email)
		obj.save()
		return HttpResponse("successfull")

	return render(request,'Student/register.html')

def show(request):
	data = student.objects.all()
	return render(request,'Student/data.html',{'data':data})

def edit(request,id):
	data = student.objects.get(id=id)
	if(request.method =='POST'):
		data.First_name=request.POST.get("fname")
		data.Last_name=request.POST.get("lname")
		data.Email=request.POST.get("email")
		data.branch=request.POST.get('branch')
		data.Age = request.POST.get('age')
		data.save()
		return redirect('show')
	return render(request,'Student/edit.html',{'data':data})


def delete(request,id):
	data = student.objects.get(id=id)
	return render(request,'student/delete.html',{'data':data})

def confirm(request,id):
	data= student.objects.get(id=id)
	data.delete()
	return redirect('show')	