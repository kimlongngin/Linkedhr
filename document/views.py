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


class DocumentDelete(SuccessMessageMixin, generic.DeleteView):
	model = Documents
	form = DocumentForm()
	template_name = 'document_delete.html'
	success_url = reverse_lazy('linkedhr:myuserprofile_without_pk')
	success_message = " Deleted successfully !"
	
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			objEdu = Documents.objects.filter(id=self.kwargs['pk'], user=request.user.id, is_status=True)
			if objEdu.count()<=0:
				return render(request, "error.html")
			self.object = self.get_object()
			return super(DocumentDelete, self).get(request, *args, **kwargs)	
			
		else:
			return redirect('linkedhr:login') 
    
	def dispatch(self, request, *args, **kwargs):
		try:
			#Br = get_object_or_404(Branch, id = self.kwargs['pk'], is_status=True)
			com = Documents.objects.get(id=self.kwargs['pk'], user= request.user.id)
			if request.user.is_authenticated():
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except Documents.DoesNotExist:
			#raise Http404("Please check user log in !") 
			return render(request, "error.html")



# This view is for update the view of the Education
class  DocumentUpdate(SuccessMessageMixin, generic.UpdateView):
	model = Documents
	success_message = "Document was updated successfully"
	form = DocumentForm()
	fields = ['title', 'file', 'description'] 
	template_name = 'document_update.html'

	def get_form(self):
		return DocumentForm(**self.get_form_kwargs())	

	def dispatch(self, request, *args, **kwargs):
		try:
			if request.user.is_authenticated():
				objDocs = Documents.objects.filter(id=self.kwargs['pk'], user=request.user.id, is_status=True)
				if objDocs.count()<=0:
					return render(request, "error.html")
				return super(self.__class__, self).dispatch(request, *args, **kwargs)	
			else:
				return redirect('linkedhr:login')  
		except Documents.DoesNotExist:
			raise Http404("You don't have permission to update this branch !") 

	def get(self, request, *args, **kwargs):
		form = DocumentForm()
		if request.user.is_authenticated():
			#objCom = Company.objects.filter(id = self.kwargs['pk'], user_id=request.user.id, is_branch=True, is_status=True)
			objDocs = Documents.objects.filter(id=self.kwargs['pk'], user=request.user.id, is_status=True)
			if objDocs.count()<=0:
				return render(request, "error.html")
			self.object = self.get_object()
			return super(DocumentUpdate, self).get(request, *args, **kwargs)	
		else:
			return redirect('linkedhr:login')  

	def get_success_url(self):
		if self.kwargs['pk']:
			return reverse_lazy('linkedhr:document-update',kwargs={'pk':self.kwargs['pk']})
		return redirect('linkedhr:myuserprofile_without_pk')



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