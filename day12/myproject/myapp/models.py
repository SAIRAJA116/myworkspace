from django.db import models

# Create your models here.

class Library(models.Model):
	branches=(('CSE','cse'),('IT','it'),
		('EEE','eee'),
		('ECE','ece'),
		('MECH','mech'),
		('CIVIL','civil'))

	Book_Number=models.IntegerField()
	Book_Name=models.CharField(max_length=50)
	Book_Author=models.CharField(max_length=50)
	Department=models.CharField(max_length=10,choices=branches)
	Publication_Date=models.DateField()