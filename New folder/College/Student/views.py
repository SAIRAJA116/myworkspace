from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'Student/home.html')

def register(request):
	if request.method == 'POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		if request.POST.get('f')=='on':
			gender ='Female'
		elif request.POST.get('m')=='on':
			gender = 'Male' 
		branch = request.POST['branch']
		

		return render(request,'Student/data.html',{'fname':fname,'lname':lname,'branch':branch,'email':email,'gender':gender})

	return render(request,'Student/register.html')