from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from .models import Documents
from linkedhr.models import UserProfile
from .forms import DocumentForm
#from linkedhr.forms import ExperienceForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User  


class DocumentCreateView(SuccessMessageMixin, CreateView):
	model = Documents 
	form = DocumentForm()
	template_name = 'document_create.html'
	success_message = "Created successfully"

	def dispatch(self, request, *args, **kwargs):	
		if request.user.is_authenticated():
			userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						return super(self.__class__, self).dispatch(request, *args, **kwargs)	
					else:
						return render(request, 'error.html')
			else:
				raise Http404("Please check user log in !") 
		else:
			return redirect('linkedhr:login')
	def get(self, request):
		form = DocumentForm()
		if request.user.is_authenticated():	
			userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						return render(request, self.template_name, {'form':form})
					else:
						return render(request, 'error.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login')

	def post(self, request):
		form = DocumentForm(request.POST, request.FILES)
		if request.user.is_authenticated():
			userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						if form.is_valid():
							documents = form.save(commit=False)
							documents.user = request.user
							documents.save()
							title = form.cleaned_data['title']
							file = form.cleaned_data['file']
							description = form.cleaned_data['description']
							messages.success(request, "Created sucessfully !")
						args = {'form':form}
						return render(request, self.template_name, args)
					else:
						return render(request, 'error.html')
			else:
				return redirect('linkedhr:userprofile')

		else:
			return redirect('linkedhr:login')