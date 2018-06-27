from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from linkedhr.models import City, UserProfile, Stage, Education
#from .forms import EducationForm
from linkedhr.forms import EducationForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User 
 

# This view is for update the view of the Education
class  EducationUpdate(SuccessMessageMixin, generic.UpdateView):
	model = Education
	success_message = "Education was updated successfully"
	form = EducationForm()
	fields = ['degree', 'institute', 'start_education_at', 'graduation_at', 'description'] 
	template_name = 'education/education_update.html'

	def get_form(self):
		return EducationForm(**self.get_form_kwargs())	

	@method_decorator(login_required(''))
	def dispatch(self, request, *args, **kwargs):
		try:
			if request.user.is_authenticated():
				objEdu = Education.objects.filter(id=self.kwargs['pk'], user_id=request.user.id, is_status=True)
				if objEdu.count()<=0:
					return render(request, "error_education_experience.html")
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except Education.DoesNotExist:
			raise Http404("You don't have permission to update this branch !") 

	@method_decorator(login_required(''))
	def get(self, request, *args, **kwargs):
		form = EducationForm()
		if request.user.is_authenticated():
			#objCom = Company.objects.filter(id = self.kwargs['pk'], user_id=request.user.id, is_branch=True, is_status=True)
			objEdu = Education.objects.filter(id=self.kwargs['pk'], user_id=request.user.id, is_status=True)
			if objEdu.count()<=0:
				return render(request, "education/error_education_experience.html")
			self.object = self.get_object()
			return super(EducationUpdate, self).get(request, *args, **kwargs)	
			
		else:
			return redirect('linkedhr:login')  

	def get_success_url(self):
		if self.kwargs['pk']:
			return reverse_lazy('linkedhr:education-update',kwargs={'pk':self.kwargs['pk']})
		return redirect('linkedhr:myuserprofile_without_pk')


class  EducationDeleteView(SuccessMessageMixin, generic.DeleteView):
	model = Education 
	form = EducationForm()
	success_url = reverse_lazy('linkedhr:myuserprofile_without_pk')
	success_message = " Deleted successfully !"
	template_name ="education/education_delete.html"

	@method_decorator(login_required(''))
	def dispatch(self, request, *args, **kwargs):
		try:
			#Br = get_object_or_404(Branch, id = self.kwargs['pk'], is_status=True)
			com = Education.objects.get(id=self.kwargs['pk'], user_id= request.user.id)
			if request.user.is_authenticated():
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except Education.DoesNotExist:
			raise Http404("Please check user log in !") 


	@method_decorator(login_required(''))
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			objEdu = Education.objects.filter(id=self.kwargs['pk'], user_id=request.user.id, is_status=True)
			if objEdu.count()<=0:
				return render(request, "error_education_experience.html")
			self.object = self.get_object()
			return super(EducationDeleteView, self).get(request, *args, **kwargs)	
			
		else:
			return redirect('linkedhr:login') 
    
class EducationView(SuccessMessageMixin, generic.TemplateView):
	model = Education 
	form = EducationForm()
	template_name ="education/education_create.html"

	@method_decorator(login_required(''))
	def dispatch(self, request, *args, **kwargs):
		try:
			userprofiledata = UserProfile.objects.get(user_id = request.user.id, is_status=True)
			if request.user.is_authenticated():
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except UserProfile.DoesNotExist:
			raise Http404("Please check user login !") 

	@method_decorator(login_required(''))
	def get(self, request):
		form = EducationForm()
		if request.user.is_authenticated():
			try:
				userprofiledata = UserProfile.objects.get(user_id = request.user.id, is_status=True)
			
			except UserProfile.DoesNotExist:
				raise Http404("Please check user login !") 

			if userprofiledata:
				if userprofiledata.is_recruit=='2':
					return render(request, self.template_name, {'form':form})
				else:
					#return redirect('linkedhr:error_education');
					return render(request, 'education/error_education_experience.html')

			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login')

	@method_decorator(login_required(''))
	def post(self, request):
		form = EducationForm(request.POST)
		if request.user.is_authenticated():
			
			if form.is_valid():
				post = form.save(commit=False)
				post.user_id = request.user
				post.save()
				majority = form.cleaned_data['majority']
				degree = form.cleaned_data['degree']
				institute = form.cleaned_data['institute']
				start_education_at = form.cleaned_data['start_education_at']
				graduation_at = form.cleaned_data['graduation_at']
				description = form.cleaned_data['description']
				messages.success(request, "Created sucessfully !")
				CreateStage = Stage.objects.create(user_id = request.user, stage=2, description='User profile registration.')
				CreateStage.save()	
				#return redirect('linkedhr:userexperience')
			#form = EducationForm()
			args = {'form':form }
			return render(request, self.template_name, args)
 		else:
 			return redirect('linkedhr:login')


