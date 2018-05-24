
from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from linkedhr.models import City, UserProfile, Stage, Branch, Company, ExperienceCheck
from linkedhr.forms import BranchForm, UserForm, UserLoginForm, UserProfileForm, EducationForm, ExperienceForm, CompanyForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User 


# ***************************************************
# ****************** BLOCK BRANCH *******************
# ***************************************************

class UpdateBranch(generic.UpdateView):
	model = Company 
	fields = ['name', 'location',  'address', 'web_site', 'email', 'phone_number', 'description'] 

# Create branch in case each company has their branch
class BranchView(generic.TemplateView):
	template_name = 'branch/branch_create.html'
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return super(self.__class__, self).dispatch(request, *args, **kwargs)	
		else:
			return redirect('linkedhr:login') 

	def get(self, request):
		form = BranchForm()
		if request.user.is_authenticated():
			objCom = Company.objects.filter(user_id=request.user.id, is_status=True)
			if objCom.count()<=0:
				return redirect('linkedhr:company')

			userprofiledata = UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata :
				for i in userprofiledata:
					if i.is_recruit=='1':
						branches = Branch.objects.all()
						args = {'form':form, 'branches':branches}
						return render(request, self.template_name, args)
					else:
						return render(request, 'company/error_company.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login')

	def post(self, request):
		form = BranchForm(request.POST)
		if request.user.is_authenticated():
			objCom = Company.objects.get(user_id=request.user.id)
			#objCom= get_object_or_404(Company, user_id = request.user.id)
			print(objCom)


			userprofiledata = UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata :
				for i in userprofiledata:
					if i.is_recruit=='1':
						if form.is_valid:
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
							
						form = BranchForm()
						args = {'form':form, 'name':name}
						#return HttpResponseRedirect(request.get_absolute_url())
						return render(request, self.template_name, args)
					else:
						return render(request, 'company/error_company.html')
			else:
				return redirect('linkedhr:userprofile')
		else:
			return redirect('linkedhr:login') 

