
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Documents
from datetime import date

class DocumentForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter tilte'}), required=False)
	file = forms.FileField(required=False)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)

	class Meta: 
		model = Documents
		fields = ['title','file', 'description']

	def clean_title(self):
		if self.cleaned_data['title'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['title']

	def clean_file(self):
		if self.cleaned_data['file'] == None:
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['file']


	#def __init__(self, *args, **kwargs):
		#super(DocumentForm, self).__init__(*args, **kwargs)
		#self.fields['file'].label='File (pdf, png, jpg, jpeg)'
