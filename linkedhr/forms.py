from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from linkedhr.models import UserProfile, Education, Experience, Company, Branch
from datetime import date

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta: 
		model = User
		fields =['username', 'first_name', 'last_name', 'email', 'password']

class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta: 
		model = User
		fields =['username', 'password']

class UserProfileForm(forms.ModelForm):
	#user_id = forms.OneToOneField(User, related_name='profile')
	description = forms.CharField(widget=forms.Textarea)

	class Meta: 
		model = UserProfile
		fields = ['sex', 'date_of_birth', 'city', 'email','phone_number', 'is_recruit', 'description']

class EducationForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)

	class Meta: 
		model = Education
		fields = ['majority','degree', 'institute', 'start_education_at', 'graduation_at', 'description']

class ExperienceForm(forms.ModelForm):
	position = forms.CharField(required=False)
	company = forms.CharField(required=False)
	description = forms.CharField(widget=forms.Textarea, required=False)

	class Meta: 
		model = Experience
		fields = ['position','company', 'start_date', 'due_date', 'description', 'is_status']

class CompanyForm(forms.ModelForm):
	name = forms.CharField()
	#company_logo = forms.FileField(required=False)
	address = forms.CharField(widget=forms.Textarea)
	description = forms.CharField(widget=forms.Textarea)

	class Meta: 
		model = Company
		fields = ['name','company_logo','email', 'phone_number','location','web_site','address','description', 'is_branch', 'is_status']

class BranchForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	address = forms.CharField(widget=forms.Textarea)
	class Meta: 
		model = Company
		fields = ['name','location','address', 'web_site', 'email','phone_number', 'description']
