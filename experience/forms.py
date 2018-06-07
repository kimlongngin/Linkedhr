
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from linkedhr.models import Experience
from datetime import date

class ExperienceForm(forms.ModelForm):
	position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter possition'}), required=True)
	company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter company'}), required=True)
	start_date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=True)
	due_date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)

	class Meta: 
		model = Experience
		fields = ['position','company', 'start_date', 'due_date', 'description']