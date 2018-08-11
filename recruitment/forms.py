from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from linkedhr.models import Recruitment, Company, Branch, Position, JobType, JobPackage
from datetime import date
from django.shortcuts import render, get_object_or_404, Http404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, logout, login

class RecruitmentForm(forms.ModelForm):
    company = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=None, required=False)

    job_package = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=None, required=False)

    branch = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=None, required=False
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title'}),
        required=False)

    position = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=None, required=False
    )
    sub_position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    salary = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    number_of_employee = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    experience = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    start_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    due_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        required=False
    )

    job_type = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=None, required=False)



    def clean_description(self):
        if self.cleaned_data['description'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['description']

    def clean_address(self):
        if self.cleaned_data['address'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['address']

    def clean_phone_number(self):
        if self.cleaned_data['phone_number'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['phone_number']

    def clean_email(self):
        if self.cleaned_data['email'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['email']

    def clean_due_date(self):
        if self.cleaned_data['due_date'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['due_date']

    def clean_start_date(self):
        if self.cleaned_data['start_date'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['start_date']

    def clean_experience(self):
        if self.cleaned_data['experience'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['experience']

    def clean_number_of_employee(self):
        if self.cleaned_data['number_of_employee'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['number_of_employee']

    def clean_salary(self):
        if self.cleaned_data['salary'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['salary']

    def clean_title(self):
        if self.cleaned_data['title'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['title']

    def clean_company(self):
        if self['company'].value() !='':
            return self.cleaned_data['company']
        raise forms.ValidationError('This field cannot be blank!')

    def clean_job_package(self):
        if self['job_package'].value() !='':
            return self.cleaned_data['job_package']
        raise forms.ValidationError('This field cannot be blank!')    

    def clean_branch(self):
        if self['branch'].value() != '':
            return self.cleaned_data['branch']
        raise forms.ValidationError('This field cannot be blank!')

    def clean_position(self):
        if self['position'].value() != '':
            return self.cleaned_data['position']
        raise forms.ValidationError('This field cannot be blank!')


    def clean_sub_position(self):
        if self.cleaned_data['sub_position'].strip() == '':
            raise forms.ValidationError('This field cannot be blank!')
        return self.cleaned_data['sub_position']

    def clean_job_type(self):
        if self['job_type'].value() != '':
            return self.cleaned_data['job_type']
        raise forms.ValidationError('This field cannot be blank!')


    class Meta:
        model = Recruitment
        fields = ['company', 'branch', 'title', 'position', 'sub_position', 'salary', 'number_of_employee',
                  'experience', 'start_date', 'due_date', 'email', 'phone_number', 'address', 'description', 'job_type']


    def __init__(self, user, *args, **kwargs):
        super(RecruitmentForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.filter(user_id = user)
        self.fields['branch'].queryset = Branch.objects.all()
        self.fields['job_package'].queryset = JobPackage.objects.all()
        self.fields['position'].queryset = Position.objects.all()
        self.fields['job_type'].queryset = JobType.objects.all()

