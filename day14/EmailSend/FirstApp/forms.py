from django.forms import ModelForm 
from .models import EmailUser

class EmailForm(ModelForm):
	class Meta:
		model=EmailUser
		fields=['fname','lname','username','email','dob']