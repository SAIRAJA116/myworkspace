from django.db import models

# Create your models here.
class EmailUser(models.Model):
	fname=models.CharField(max_length = 50)
	lname=models.CharField(max_length = 50)
	username=models.CharField(max_length = 50,unique=True)
	email=models.EmailField()
	dob=models.DateField(null=True,blank=True)
	password = models.CharField(max_length=50)
	