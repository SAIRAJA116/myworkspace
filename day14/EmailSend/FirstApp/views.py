from django.shortcuts import render
from EmailSend import  settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import EmailUser
from .forms import EmailForm
import random
# Create your views here.
def mail(request):
	if request.method=='POST':
		tomail=request.POST['email']
		sub=request.POST['sub']
		msg=request.POST['msg']
		sender = settings.EMAIL_HOST_USER
		receiver=tomail
		email=EmailMessage(sub,msg,sender,[receiver])
		email.content_subtype='html'
		file = request.FILES['file']
		email.attach(file.name,file.read(),file.content_type)
		email.send()
		return HttpResponse("sent")


	return render(request,'mail.html')






def register(request):
	form = EmailForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		if request.method=='POST':
			fname=request.POST['fname']
			lname=request.POST['lname']
			username=request.POST['username']
			email = request.POST['email']
			dob= request.POST['dob']
			pwd=str(random.randint(100000,999999))
			print(pwd)	
			try:
				EmailUser.objects.create(fname=fname,lname=lname,username=username,email=email,dob=dob,password=pwd)
			except:
				return HttpResponse("user already exit")
			receiver=data.email
			sender= settings.EMAIL_HOST_USER
			sub = "login details"
			body="Hello "+username+"\n\n This is your Username\n\n your password"+pwd
			mail=EmailMessage(sub,body,sender,[receiver])
			mail.send()
			return HttpResponse("please check your email")
	form=EmailForm()
	return render(request,'register.html',{'myform':form})




def login(request):
	if request.method == 'POST':
		username=request.POST['username']
		pwd = request.POST['password']
		data=EmailUser.objects.all().filter(username=username,password=pwd)
		if data:
			return render(request,'welcome.html',{'user':username})
		else:
			return HttpResponse("Invalid username or password")
	return render(request,"login.html")


def forgetpwd(request):
	if request.method == 'POST':
		email = request.POST['email']
		data=EmailUser.objects.get(email = email)
		print(data.username)
		sender = settings.EMAIL_HOST_USER
		sub= "forgetpwd"
		receiver=email
		body="hello "+data.username+"your password is"+data.password
		mail=EmailMessage(sub,body,sender,[receiver])
		mail.send()
		


	return render(request,"forgetpwd.html")

def changepwd(request):
	if(request.method == "POST"):
		oldpass = request.POST['oldpass']
		newpass = request.POST['newpass']
		conpass = request.POST['conpass']
		data = EmailUser.objects.get(password=oldpass)
		if newpass != conpass:
			return HttpResponse("password doesnot match")
		else:
			data.password = newpass
			data.save()
			return HttpResponse("your password is updated")

	return render(request,"changepwd.html")	

'''if request.method=='POST':
fname=request.POST['fname']
lname=request.POST['lname']
username=request.POST['username']
email = request.POST['email']
dob= request.POST['dob']
pwd=str(random.randint(100000,999999))'''

'''
def register(request):
	form = EmailForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		data = EmailUser.objects.get(fname = request.POST['fname'])
		pwd=str(random.randint(100000,999999))
		data.password = pwd
		data.save()
		print(data)
		receiver=data.email
		sender= settings.EMAIL_HOST_USER
		sub = "login details"
		body="Hello "+username+"\n\n This is your Username\n\n your password"+pwd
		mail=EmailMessage(sub,body,sender,[receiver])
		mail.send()
		return HttpResponse("please check your email")
	form=EmailForm()
	return render(request,'register.html',{'myform':form})
'''