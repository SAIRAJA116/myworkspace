from django.db import models

# Create your models here.
class student(models.Model):
	First_name = models.CharField(max_length=30)
	Last_name= models.CharField(max_length=30)
	branch = models.CharField(max_length=10)
	Age = models.IntegerField()
	Email = models.EmailField()

	def __str__(self):
		return self.First_name+" " +self.Last_name


	class Meta:
		verbose_name_plural = 'student'
		db_table = 'Collegestudent'