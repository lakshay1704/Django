from django.forms import ModelForm,TextInput
from .models import City

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ['name'] #in this statement all the conditions of the name field as in the model 
								#is used and inherited from the model
		widgets = {'name':TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})} #this lets you add from the css and html sides