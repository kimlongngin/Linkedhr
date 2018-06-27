from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from linkedhr.models import City, UserProfile, Stage, Experience
from .forms import ExperienceForm
#from linkedhr.forms import ExperienceForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User  


class ExperienceDeleteView(SuccessMessageMixin, DeleteView):
	model = Experience 
	form = ExperienceForm()
	success_url = reverse_lazy('linkedhr:myuserprofile_without_pk')
	success_message = " Deleted successfully !"
	template_name ="experience/experience_delete.html"

	@method_decorator(login_required(''))
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			objEx= Experience.objects.filter(id=self.kwargs['pk'], user_id=request.user.id, is_status=True)
			if objEx.count()<=0:
				return render(request, "error_education_experience.html")
			self.object = self.get_object()
			return super(ExperienceDeleteView, self).get(request, *args, **kwargs)	
		else:
			return redirect('linkedhr:login') 

	@method_decorator(login_required(''))
	def dispatch(self, request, *args, **kwargs):	
		if request.user.is_authenticated():
			userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						return super(self.__class__, self).dispatch(request, *args, **kwargs)	
					else:
						return render(request, 'error_education_experience.html')
			else:
				raise Http404("Please check user log in !") 
		else:
			return redirect('linkedhr:login')

class  ExperienceUpdate(SuccessMessageMixin, UpdateView):
	model = Experience 
	form = ExperienceForm()
	template_name = 'experience/experience_update.html'
	success_message = "Experience was updated successfully"
	fields = ['position', 'company', 'start_date', 'due_date', 'description'] 

	def get_form(self):
		return ExperienceForm(**self.get_form_kwargs())

	@method_decorator(login_required(''))
	def dispatch(self, request, *args, **kwargs):	
		form = ExperienceForm()	
		if request.user.is_authenticated():
			userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						return super(self.__class__, self).dispatch(request, *args, **kwargs)	
					else:
						return render(request, 'error_education_experience.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login') 

	@method_decorator(login_required(''))
	def get(self, request, *args, **kwargs):
		form = ExperienceForm()
		if request.user.is_authenticated():			
			self.object = self.get_object()
			return super(ExperienceUpdate, self).get(request, *args, **kwargs)
		else:
			return redirect('linkedhr:login')

	def get_success_url(self):
		if self.kwargs['pk']:
			return reverse_lazy('linkedhr:experience-update',kwargs={'pk':self.kwargs['pk']})
		return redirect('linkedhr:myuserprofile_without_pk')

class ExperienceView(SuccessMessageMixin, TemplateView):
	model = Experience 
	form = ExperienceForm()
	template_name ="experience/experience_create.html"
	
	@method_decorator(login_required(''))
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						return super(self.__class__, self).dispatch(request, *args, **kwargs)
					else:	
						return render(request, 'userprofile/error_education_experience.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login')

	@method_decorator(login_required(''))		
	def get(self, request):
		form = ExperienceForm()
		if request.user.is_authenticated():	
			userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						return render(request, self.template_name, {'form':form})
					else:
						return render(request, 'userprofile/error_education_experience.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login')

	@method_decorator(login_required(''))
	def post(self, request):
		form = ExperienceForm(request.POST)
		if request.user.is_authenticated():
			if form.is_valid():
				post = form.save(commit=False)
				post.user_id = request.user
				post.save()
				position = form.cleaned_data['position']
				company = form.cleaned_data['company']
				start_date = form.cleaned_data['start_date']
				due_date = form.cleaned_data['due_date']
				description = form.cleaned_data['description']
				
				CreateStage = Stage.objects.create(user_id = request.user, stage=3, description='User profile registration.')
				UserProfile.objects.filter(user_id=request.user.id).update(authority=True)
				CreateStage.save()	
				messages.success(request, "Created sucessfully !")
				form.save()
				form = ExperienceForm()
			#form = ExperienceForm()				
			args = {'form':form}
			return render(request, self.template_name, args)
		else:
			return redirect('linkedhr:login')





 
