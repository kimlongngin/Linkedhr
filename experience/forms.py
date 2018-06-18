
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from linkedhr.models import Experience
from datetime import date

class ExperienceForm(forms.ModelForm):
	position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter possition'}), required=False)
	company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter company'}), required=False)
	start_date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=False)
	due_date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=False)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)

	class Meta: 
		model = Experience
		fields = ['position','company', 'start_date', 'due_date', 'description']
	def clean_position(self):
		if self.cleaned_data['position'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['position']

	def clean_company(self):
		if self.cleaned_data['company'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['company']
	def clean_start_date(self):
		if self.cleaned_data['start_date'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['start_date']
	def clean_due_date(self):
		if self.cleaned_data['due_date'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['due_date']