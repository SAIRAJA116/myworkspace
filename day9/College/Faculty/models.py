from django.db import models

# Create your models here.
class faculty(models.Model):
	branches=(
		('ece','ECE'),
		('cse','CSE'),
		('it','IT'),
		('me','ME'),
		('ce','CIVIL')
		)
	Name = models.CharField(max_length=30)
	Qualifications = models.CharField(max_length=20,blank=True,null=True)
	Department = models.CharField(max_length=10,choices=branches)
	Email=models.EmailField(default="abc@gmail.com")
	Phone = models.CharField(max_length=10,help_text="8919227696")

	def __str__(self):
		return self.Name

	class Meta:
		verbose_name_plural = 'faculty'
		db_table = 'Collegefaculty'