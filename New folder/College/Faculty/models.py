from django.db import models

# Create your models here.
class faculty(models.Model):
	branches = (('cse','CSE'),('it','IT'),('ece','ECE'),
		('me',"ME"))
	name = models.CharField(max_length=30)
	Qulification = models.CharField(max_length=30,blank=True,null=True)
	department = models.CharField(max_length=10,choices=branches)
	Email = models.EmailField(default="abc@gmail.com",null=True)
	phone = models.CharField(max_length=10,help_text="9999999999")

def __str__(self):
	return self.name
