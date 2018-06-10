
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Documents
from datetime import date

class DocumentForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter tilte'}), required=True)
	file = forms.FileField(required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)

	class Meta: 
		model = Documents
		fields = ['title','file', 'description']

