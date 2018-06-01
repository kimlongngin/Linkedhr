from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from linkedhr.models import UserProfile, Education, Experience, Company, Branch, City
from datetime import date

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}), required=True)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter first name'}), required=True)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter last name'}), required=True)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@mail.com'}), required=True)
	password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}), required=True)
	confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}), required=True)

	class Meta: 
		model = User
		fields =['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

	def clean_confirm_password(self):
		pas= self.cleaned_data['password']
		cpas= self.cleaned_data['confirm_password']
		MIN_LENGHT = 8
		if pas and cpas:
			if pas != cpas:
				raise forms.ValidationError("password and confirm password not matched")
			else:
				if len(pas) < MIN_LENGHT:
					raise forms.ValidationError("password should have atleast 8 character")


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
	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'(86)10123456'}), required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)
	present_address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=False)
	#is_recruit = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	is_recruit = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=IS_RECRUITE), required=True)

	class Meta: 
		model = UserProfile
		fields = ['sex', 'date_of_birth', 'country', 'city', 'nationality','email','phone_number','present_address', 'description', 'is_recruit']
	
	#def __init__(self, *args, **kwargs):
		#super(UserProfileForm, self).__init__(*args, **kwargs)
		#self.fields['city'].queryset = City.objects.all()
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class CompanyForm(forms.ModelForm):
	company_logo= forms.FileField(required=False)
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter country name'}), required=True)
	web_site =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@mail.com'}), required=True)
	address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':"3"}), required=True)
	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'(86)10123456'}), required=True)
	location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter city name'}), required=True)
	is_branch = forms.BooleanField(required=False)
	class Meta: 
		model = Company
		fields = ['name','company_logo','web_site','email', 'phone_number','location','address','description', 'is_branch']

	def __init__(self, *args, **kwargs):
		super(CompanyForm, self).__init__(*args, **kwargs)
		self.fields['is_branch'].label='Doese your company has more branch ?'
		self.fields['is_branch'].widget.attrs['type']='checkbox'
		self.fields['is_branch'].widget.attrs['class']='checkbox'
		self.fields['company_logo'].widget.attrs['type']='file'
		self.fields['name'].label='Name(*)'


	

class EducationForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)

	class Meta: 
		model = Education
		fields = ['majority','degree', 'institute', 'start_education_at', 'graduation_at', 'description']

class ExperienceForm(forms.ModelForm):
	position = forms.CharField(required=True)
	company = forms.CharField(required=True)
	description = forms.CharField(widget=forms.Textarea, required=False)

	class Meta: 
		model = Experience
		fields = ['position','company', 'start_date', 'due_date', 'description', 'is_status']


class BranchForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	address = forms.CharField(widget=forms.Textarea)
	class Meta: 
		model = Branch
		fields = ['com_id', 'name','location','address', 'web_site', 'email','phone_number', 'description']
