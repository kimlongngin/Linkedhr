from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from linkedhr.models import City, UserProfile, Stage, Branch, Company, ExperienceCheck
#from linkedhr.forms import BranchForm, UserForm, UserLoginForm, UserProfileForm, ExperienceForm, CompanyForm
from linkedhr.forms import BranchForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User 


class  BranchDeleteView(SuccessMessageMixin, DeleteView):
	model = Branch 
	form = BranchForm()
	success_url = reverse_lazy('linkedhr:myuserprofile_without_pk')
	success_message = " Deleted successfully !"
	template_name ="branch/branch_delete.html"

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			objCom = Company.objects.filter(branch__id=self.kwargs['pk'], user_id=request.user.id, is_branch=True, is_status=True)
			if objCom.count()<=0:
				return render(request, "branch/error_branch.html", {'arg':self.kwargs['pk']})
			self.object = self.get_object()
			return super(BranchDeleteView, self).get(request, *args, **kwargs)	
			
		else:
			return redirect('linkedhr:login') 
    
	def dispatch(self, request, *args, **kwargs):
		try:
			#Br = get_object_or_404(Branch, id = self.kwargs['pk'], is_status=True)
			com = Company.objects.get(branch__id=self.kwargs['pk'], user_id= request.user.id)
			if request.user.is_authenticated():
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except Company.DoesNotExist:
			raise Http404("You don't have permission to delete this branch !") 

class UpdateBranchView(SuccessMessageMixin, UpdateView):
	model = Branch 
	form = BranchForm()
	template_name = 'branch/branch_update.html'
	fields = ['name', 'location',  'address', 'web_site', 'email', 'phone_number', 'description'] 
	success_message = "Updated successfully"

	def get_form(self):
		return BranchForm(**self.get_form_kwargs())

	def dispatch(self, request, *args, **kwargs):
		try:
			#Br = Branch.objects.get(id = self.kwargs['pk'], is_status)
			#Br = get_object_or_404(Branch, id = self.kwargs['pk'], is_status=True)
			#com = Company.objects.get(id = Br.com_id, user_id= request.user.id)
			com = Company.objects.get(branch__id=self.kwargs['pk'], user_id= request.user.id)
			if request.user.is_authenticated():
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except Company.DoesNotExist:
			raise Http404("You don't have permission to update this branch !") 

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			#objCom = Company.objects.filter(id = self.kwargs['pk'], user_id=request.user.id, is_branch=True, is_status=True)
			objCom = Company.objects.filter(branch__id=self.kwargs['pk'], user_id=request.user.id, is_branch=True, is_status=True)
			if objCom.count()<=0:
				return render(request, "branch/error_branch.html", {'arg':self.kwargs['pk']})
			self.object = self.get_object()
			return super(UpdateBranchView, self).get(request, *args, **kwargs)	
			
		else:
			return redirect('linkedhr:login')  
		

	def get_success_url(self):
		if self.kwargs['pk']:
			return reverse_lazy('linkedhr:branch-update',kwargs={'pk':self.kwargs['pk']})
		return redirect('linkedhr:myuserprofile_without_pk')
   



# Create branch in case each company has their branch
class BranchView(SuccessMessageMixin, generic.TemplateView):
	model = Branch
	template_name = 'branch/branch_create.html'
	fields = ['name', 'location',  'address', 'web_site', 'email', 'phone_number', 'description'] 

	def dispatch(self, request, *args, **kwargs):
		form = BranchForm()
		

		try:
			com = Company.objects.get(id = self.kwargs['pk'], user_id= request.user.id, is_branch=True)
			if request.user.is_authenticated():
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except Company.DoesNotExist:
			#raise Http404("You don't have permission to create branch !")
			return render(request, "branch/error_branch.html", {'arg':self.kwargs['pk']})
	
	def get(self, request, pk):
		form = BranchForm()
		if request.user.is_authenticated():
			objCom = Company.objects.filter(id = self.kwargs['pk'], user_id=request.user.id, is_branch=True, is_status=True)
			if objCom.count()<=0:
				#return render('linkedhr:error_branch', self.kwargs['pk'])
				return render(request, "branch/error_branch.html", {'arg':self.kwargs['pk']})

			userprofiledata = UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata :
				for i in userprofiledata:
					if i.is_recruit=='1':
						#branches = Branch.objects.all()
						args = {'form':form}
						return render(request, self.template_name, args)
					else:
						return render(request, 'company/error_company.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login')

	def post(self, request, pk):
		form = BranchForm(request.POST)
		if request.user.is_authenticated():
			try:
				objCom = Company.objects.get(id = self.kwargs['pk'], user_id=request.user.id, is_branch=True, is_status=True)
			except Company.DoesNotExist:
				#raise Http404("You don't have permission to create branch !")
				return render(request, "branch/error_branch.html", {'arg':self.kwargs['pk']})
			userprofiledata = UserProfile.objects.filter(user_id = request.user.id, is_status=True)
			if userprofiledata :
				for i in userprofiledata:
					if i.is_recruit=='1':
						if form.is_valid():
							branch = form.save(commit = False)
							branch.com_id = objCom
							branch.save()
							name = form.cleaned_data['name']
							location = form.cleaned_data['location']
							address = form.cleaned_data['address']
							web_site = form.cleaned_data['web_site']
							email = form.cleaned_data['email']
							phone_number = form.cleaned_data['phone_number']
							description = form.cleaned_data['description']
							messages.success(request, "Created sucessfully !")
						
						#form = BranchForm()
						args = {'form':form}
						#return HttpResponseRedirect(request.get_absolute_url())
						return render(request, self.template_name, args)
					else:
						return render(request, 'company/error_company.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login') 

