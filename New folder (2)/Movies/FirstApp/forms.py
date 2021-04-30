from django.forms import ModelForm 
from .models import Movie

class MovieForm(ModelForm):
	class Meta:
		model=Movie
		fields=['moviename','heroname','heroinname','poster']