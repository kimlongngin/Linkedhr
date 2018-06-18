from django.contrib.auth.models import User
from django import forms
from django.core.validators import validate_email
from django.forms import ModelForm
from linkedhr.models import UserProfile, Education, Experience, Company, Branch, City
from datetime import date
from django.shortcuts import render, get_object_or_404, Http404



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

	majority = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your majority'}), required=False)
	degree = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=IS_DEGREE), required=False)
	institute = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your majority'}), required=False)
	start_education_at= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=False)
	graduation_at= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=False)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)

	class Meta: 
		model = Education
		fields = ['institute', 'majority','degree', 'start_education_at', 'graduation_at', 'description']

	def clean_majority(self):
		if self.cleaned_data['majority'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['majority']	
	def clean_degree(self):
		if self.cleaned_data['degree'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['degree']		
	def clean_institute(self):
		if self.cleaned_data['institute'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['institute']
	def clean_start_education_at(self):
		if self.cleaned_data['start_education_at'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['start_education_at']
	def clean_graduation_at(self):
		if self.cleaned_data['graduation_at'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['start_education_at']


class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}), required=False)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter first name'}), required=False)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter last name'}), required=False)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@mail.com'}), required=False)
	password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}), required=False)
	confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}), required=False)

	class Meta: 
		model = User
		fields =['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

	def clean_username(self):
		if self.cleaned_data['username'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['username']
	def clean_first_name(self):
		if self.cleaned_data['first_name'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['first_name']
	def clean_last_name(self):
		if self.cleaned_data['last_name'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['last_name']
	
	def clean_password(self):
		if self.cleaned_data['password'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['password']
		
	def clean_confirm_password(self):
		if self.cleaned_data['confirm_password'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		pas= self.cleaned_data['password']
		cpas= self.cleaned_data['confirm_password']
		MIN_LENGHT = 8
		if pas and cpas:
			if pas != cpas:
				raise forms.ValidationError("password and confirm password not matched")
			else:
				if len(pas) < MIN_LENGHT:
					raise forms.ValidationError("password should have atleast 8 character")
	def clean_email(self):
		if self.cleaned_data['email'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		email = self.cleaned_data['email']
		try:
			mt = validate_email(email)
		except:
			return forms.ValidationError("Email is not in correct format")
		return email

class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta: 
		model = User
		fields =['username', 'password']

TITLE_CHOICES = (
	('', '-------------------'),
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
IS_RECRUITE = (
	('', '-------------------'),
    ('1', 'Recruiter'),
    ('2', 'Seeker'),
)

class UserProfileForm(forms.ModelForm):

	sex = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=TITLE_CHOICES), required=True)
	date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}), required=True)
	country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter country name'}), required=True)
	city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter city name'}), required=True)
	#city = forms.ModelMultipleChoiceField(queryset=None)
	#city = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}), queryset=None, required=True)
	nationality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kh'}), required=False)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@mail.com'}), required=True)
	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'85510123456'}), required=True)
	zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'zip code'}), required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)
	present_address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)
	#is_recruit = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	is_recruit = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=IS_RECRUITE), required=True)

	class Meta: 
		model = UserProfile
		fields = ['sex', 'date_of_birth', 'country', 'city', 'nationality','email','phone_number','zip_code','present_address', 'description', 'is_recruit']
	
	def clean_zip_code(self):
		zipc = self.cleaned_data.get('zip_code', None)
		try:
			int(zipc)
		except (ValueError, TypeError):
			raise forms.ValidationError('Make sure that this field can input only number.')
		return zipc

	def clean_phone_number(self):
		phone_no = self.cleaned_data.get('phone_number', None)
		try:
			int(phone_no)
		except (ValueError, TypeError):
			raise forms.ValidationError('Please enter a valid phone number')
		return phone_no
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			mt = validate_email(email)
		except:
			return forms.ValidationError("Email is not in correct format")
		return email
	#def __init__(self, *args, **kwargs):
		#super(UserProfileForm, self).__init__(*args, **kwargs)
		#self.fields['city'].queryset = City.objects.all()


class BranchForm(forms.ModelForm):
	#com_id = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}), queryset=None, required=True)
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter branch name'}), required=False)
	location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter location'}), required=False)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@mail.com'}), required=False)
	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'(86)10123456'}), required=False)
	web_site=forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Enter website'}), required=False)
	address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)
	class Meta: 
		model = Branch
		fields = ['name','location','address', 'web_site', 'email','phone_number', 'description']
	def clean_name(self):
		if self.cleaned_data['name'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['name']
	def clean_location(self):
		if self.cleaned_data['location'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['location']

	def clean_email(self):
		if self.cleaned_data['email'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['email']

	def clean_phone_number(self):
		if self.cleaned_data['phone_number'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['phone_number']

	def clean_web_site(self):
		if self.cleaned_data['web_site'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['web_site']
	def clean_address(self):
		if self.cleaned_data['address'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['address']
	def clean_description(self):
		if self.cleaned_data['description'].strip() == '':
			raise forms.ValidationError('This field cannot be blank!')
		return self.cleaned_data['description']


	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			mt = validate_email(email)
		except:
			return forms.ValidationError("Email is not in correct format")
		return email
	#def __init__(self, *args, **kwargs):
		#super(BranchForm, self).__init__(*args, **kwargs)
		#self.fields['com_id'].queryset = Company.objects.all()	
	


class ExperienceForm(forms.ModelForm):
	position = forms.CharField(required=True)
	company = forms.CharField(required=True)
	description = forms.CharField(widget=forms.Textarea, required=False)

	class Meta: 
		model = Experience
		fields = ['position','company', 'start_date', 'due_date', 'description', 'is_status']

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class CompanyForm(forms.ModelForm):
    company_logo = forms.FileField(required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country name'}),
                           required=False)
    web_site = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
                            required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': "3"}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': "3"}), required=False)
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(86)10123456'}), required=False)
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city name'}), required=False)
    is_branch = forms.BooleanField(required=False)

    class Meta:
        model = Company
        fields = ['name', 'company_logo', 'web_site', 'email', 'address', 'phone_number', 'location', 'is_branch', 'description']

    def clean_phone_location(self):
        if self.cleaned_data['location'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['location']

    def clean_phone_location(self):
        if self.cleaned_data['location'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['location']

    def clean_phone_number(self):
        if self.cleaned_data['phone_number'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['phone_number']

    def clean_address(self):
        if self.cleaned_data['address'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['address']

    def clean_email(self):
        if self.cleaned_data['email'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['email']

    def clean_name(self):
        if self.cleaned_data['name'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['name']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['is_branch'].label = 'Doese your company has more branch ?'
        self.fields['is_branch'].widget.attrs['type'] = 'checkbox'
        self.fields['is_branch'].widget.attrs['class'] = 'checkbox'
        self.fields['company_logo'].widget.attrs['type'] = 'file'
        self.fields['name'].label = 'Name(*)'

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mt = validate_email(email)
        except:
            return forms.ValidationError("Email is not in correct format")
        return email




