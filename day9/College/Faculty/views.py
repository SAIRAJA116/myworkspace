from django.shortcuts import render
from .models import faculty
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method == 'POST':
		name=request.POST.get('name')
		qualification=request.POST.get('qua')
		email=request.POST.get('email')
		branch = request.POST.get('branch')
		ph = request.POST.get('phone')
		

		o = faculty(Name=name,Qualifications=qualification,Department=branch,Email=email,Phone=ph)
		o.save()		
		return HttpResponse("successfull")

	return render(request,'Faculty/register.html')