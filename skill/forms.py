from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from linkedhr.models import Skill
from datetime import date
from django.shortcuts import render, get_object_or_404, Http404


class SkillForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter tilte'}), required=False)
	#title = forms.CharField(required=False)
	
	class Meta:
		model = Skill
		fields = ['title']

	def clean_title(self):
		if self.cleaned_data['title'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['title']
