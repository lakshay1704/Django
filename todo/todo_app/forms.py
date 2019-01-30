'''from .models import todo
from django import forms 

class todo_form(forms.ModelForm):
	fields = ['text','completed']
'''

from django import forms

class todo_form(forms.Form):
	text = forms.CharField(max_length = 40,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'enter todo','aria-label':'Todo','aria-describedby':'add-btn'}))