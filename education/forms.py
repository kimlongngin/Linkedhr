from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from linkedhr.models import Education
from datetime import date

class EducationForm(forms.ModelForm):

	#  Degree Has relationship with user one-many  
	IS_DEGREE = (
		('', '-------------------'),
	    ('1', 'POS_DOC'),
	    ('2', 'PHD'),
	    ('3', 'MS'),
	    ('4', 'BC'),
	    ('5', 'Other'),
	)

	majority = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your majority'}), required=True)
	degree = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=IS_DEGREE), required=True)
	institute = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your majority'}), required=True)
	start_education_at= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=True)
	graduation_at= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)

	class Meta: 
		model = Education
		fields = ['institute', 'majority','degree', 'start_education_at', 'graduation_at', 'description']

