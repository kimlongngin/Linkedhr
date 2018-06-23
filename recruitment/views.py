from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from linkedhr.models import City, UserProfile, Stage, Experience, Recruitment
from .forms import RecruitmentForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User  

class RecruitmentCreateView(SuccessMessageMixin, CreateView):
	model = Recruitment
	form = RecruitmentForm()
	template_name = 'recruitment_create.html'
	success_message = " Created successfully !"
	fields = ['company', 'branch', 'title', 'position', 'sub_position', 'salary', 'number_of_employee', 'experience', 'start_date', 'due_date', 'email', 'phone_number', 'address', 'description']

	def dispatch(self, request, *args, **kwargs):
		form = RecruitmentForm()
		if request.user.is_authenticated():
			return super(self.__class__, self).dispatch(request, *args, **kwargs)	
		else:
			return redirect('linkedhr:login') 
		
		