from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
# For user registration
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from .models import City, UserProfile, Education, Stage, Experience, Branch, Company, ExperienceCheck
from .forms import BranchForm, UserForm, UserLoginForm, UserProfileForm, EducationForm, ExperienceForm, CompanyForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User 


# ***************************************************
# ****************** BLOCK BRANCH *******************
# ***************************************************

class UpdateBranch(UpdateView):
	model = Company 
	fields = ['name', 'location',  'address', 'web_site', 'email', 'phone_number', 'description'] 

# Create branch in case each company has their branch
class BranchView(TemplateView):
	template_name = 'branch/branch_create.html'
	
	def get(self, request):
		form = BranchForm()
		branches = Branch.objects.all()
		args = {'form':form, 'branches':branches}
		return render(request, self.template_name, args)

	def post(self, request):
		form = BranchForm(request.POST)

		if form.is_valid:
			#post = form.save(commit=False)
			#post.user_id = request.user
			#post.save()
			name = form.cleaned_data['name']
			location = form.cleaned_data['location']
			address = form.cleaned_data['address']
			web_site = form.cleaned_data['web_site']
			email = form.cleaned_data['email']
			phone_number = form.cleaned_data['phone_number']
			description = form.cleaned_data['description']
			is_status = form.cleaned_data['is_status']

			return redirect('linkedhr:index')
		
		args = {'form':form, 'text':text}
		return render(request, self.template_name, args)






# ***************************************************
# **************** BLOCK ExPERIENCE *****************
# ***************************************************
#class CompanyView(generic.CreateView)`:
	#model = Experience 
	#success_url = reverse_lazy('linkedhr:detailuserprofile')
	#fields = ['user_id', 'name', 'location', 'company_logo', 'email', 'phone_number','description', 'is_status']


# ********* Display of the company branch ***********
class ListCompanyView(generic.ListView):
	template_name =  'company/list_company.html'
	context_object_name = 'all_companies'
	paginate_by = 10
	def get_queryset(self):
		return Company.objects.filter(user_id=self.request.user.id);

# ********* Update Branch of the company ************
class  CompanyUpdateView(UpdateView):
	model = Company 
	fields = ['name', 'company_logo', 'email', 'phone_number', 'location', 'address', 'web_site', 'description', 'is_branch', 'is_status'] 


# *********** Add Company ***************************
class CompanyView(TemplateView):
	template_name = 'company/company_create.html'
	#form = UserProfileForm
	
	def get(self, request, *args, **kwargs):
		form = UserProfileForm()
		company = Company.objects.all()
		args = {'form':form, 'company':company}

		userprofiledata = UserProfile.objects.filter(user_id = request.user.id)
		if userprofiledata :
			return render(request, self.template_name, args)
		else:
			return redirect('linkedhr:login')
			#return render(request, self.template_name, args)

	#def get(self, request):
		#form = CompanyForm()
		#company = Company.objects.all()
		#args = {'form':form, 'company':company}
		#return render(request, self.template_name, args)
		
	def post(self, request):
		form = CompanyForm(request.POST, request.FILES)
		if request.user.is_authenticated():
			userprofiledata = UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata :

				if form.is_valid:
					post = form.save(commit=False)
					post.user_id = request.user
					post.save()
					name = form.cleaned_data['name']
					company_logo = form.cleaned_data['company_logo']
					email = form.cleaned_data['email']
					phone_number = form.cleaned_data['phone_number']
					location = form.cleaned_data['location']
					address = form.cleaned_data['address']
					web_site = form.cleaned_data['web_site']
					description = form.cleaned_data['description']
					is_branch = form.cleaned_data['is_branch']
					is_status = form.cleaned_data['is_status']
					
					if is_branch == True:
						return redirect('linkedhr:branch')
					# form = CompanyForm()
					# return redirect('linkedhr:index')
				
				args = {'form':form, 'name':name}
				return render(request, self.template_name, args)
			else:
				return redirect('linkedhr:login')
		else:
			return redirect('linkedhr:login')

# ***************************************************
# **************** BLOCK ExPERIENCE *****************
# ***************************************************


# This view is for update the experience 
#class ExperienceView(generic.CreateView):
	#model = Experience 
	#success_url = reverse_lazy('linkedhr:detailuserprofile')
	#fields = ['user_id', 'position', 'company', 'start_date', 'due_date', 'description','is_status']

class ExperienceView(TemplateView):
	template_name = 'experience/experience_create.html'
	#form = UserProfileForm
	
	def get(self, request):
		form = ExperienceForm()
		StageData= Stage.objects.filter(user_id = request.user.id, stage=2)
		userprofiledata= UserProfile.objects.filter(user_id = request.user.id)
		#IsEx = ExperienceCheck.objects.filter(user_id = request.user.id, is_experience=True)
		
		#args = {'form':form,'IsEx':IsEx}	
		if userprofiledata.count()>0:
			if StageData.count()>0:
				for i in userprofiledata:
					if i.is_recruit=='2':
						return render(request, self.template_name, {'form':form})
						
						#if IsEx.count()>0:
							#return render(request, self.template_name, {'form':form})
						#else:
							#return render(request, self.template_name, args)
					else:
						return render(request, 'userprofile/error_education_experience.html')
			else:
				return redirect('linkedhr:usereducation')			
		else:
			return redirect('linkedhr:userprofile')

	def post(self, request):
		form = ExperienceForm(request.POST)
		if request.user.is_authenticated():
			if form.is_valid:
				post = form.save(commit=False)
				post.user_id = request.user
				post.save()
				position = form.cleaned_data['position']
				company = form.cleaned_data['company']
				start_date = form.cleaned_data['start_date']
				due_date = form.cleaned_data['due_date']
				description = form.cleaned_data['description']
				is_status = form.cleaned_data['is_status']
				
				CreateStage = Stage.objects.create(user_id = request.user, stage=3, description='User profile registration.')
				UserProfile.objects.filter(user_id=request.user.id).update(authority=True)
				CreateStage.save()	
				return redirect('linkedhr:index')
			
			args = {'form':form, 'text':text}
			return render(request, self.template_name, args)
		else:
			return redirect('linkedhr:login')

# ************ Update Experience *******************
# This view is for update the view of the Education
class  ExperienceUpdate(SuccessMessageMixin, UpdateView):
	model = Experience 
	success_message = "Experience was updated successfully"
	fields = ['position', 'company', 'start_date', 'due_date', 'description'] 


# ***************************************************
# ************* BLOCK EDUCATION PROFILE *************
# ***************************************************

# This view is for create the view and insert data in to table Education
#class EducationView(generic.CreateView):
	#model = Education 
	#success_url = reverse_lazy('linkedhr:userexperience')
	#fields = ['user_id', 'degree', 'institute', 'start_education_at', 'graduation_at', 'description', 'is_status']

class EducationView(TemplateView):
	template_name = 'education/education_create.html'
	
	def get(self, request):
		form = EducationForm()
		userprofiledata = UserProfile.objects.filter(user_id = request.user.id)
		if userprofiledata :
			for i in userprofiledata:
				if i.is_recruit=='2':
					return render(request, self.template_name, {'form':form})
				else:
					#return redirect('linkedhr:error_education');
					return render(request, 'userprofile/error_education_experience.html')

		else:
			return redirect('linkedhr:userprofile')

	def post(self, request):
		form = EducationForm(request.POST)
		if request.user.is_authenticated():
			if form.is_valid:
				post = form.save(commit=False)
				post.user_id = request.user
				post.save()
				majority = form.cleaned_data['majority']
				degree = form.cleaned_data['degree']
				institute = form.cleaned_data['institute']
				start_education_at = form.cleaned_data['start_education_at']
				graduation_at = form.cleaned_data['graduation_at']
				description = form.cleaned_data['description']
				
				CreateStage = Stage.objects.create(user_id = request.user, stage=2, description='User profile registration.')
				CreateStage.save()	

				return redirect('linkedhr:userexperience')
			
			args = {'form':form, 'text':text}
			return render(request, self.template_name, args)
 		else:
 			return redirect('linkedhr:login')

# This view is for update the view of the Education
class  EducationUpdate(SuccessMessageMixin, UpdateView):
	model = Education 
	success_message = "Education was updated successfully"
	fields = ['degree', 'institute', 'start_education_at', 'graduation_at', 'description', 'is_status'] 






# ***************************************************
# ************* BLOCK USER PROFILE ******************
# ***************************************************

## Clase for registration user_profile (Create User)

#class  UserProfileView(SuccessMessageMixin, CreateView):
	#model = UserProfile 
	#success_url = reverse_lazy('linkedhr:usereducation')
	#success_message = "User Profile was created successfully"
	#fields = ['user_id', 'sex', 'date_of_birth', 'city', 'phone_number', 'is_recruit', 'is_status']
	#user_pk = model.pk
	
	#obj = UserProfileSession(user_pk)
	#obj.StoreUserProfileSess()

class UserProfileView(TemplateView):
	template_name = 'userprofile/user_create.html'
	#form = UserProfileForm
	def get(self, request, *args, **kwargs):
		form = UserProfileForm()
		
		if request.user.is_authenticated():

			userprofiledata = UserProfile.objects.filter(user_id = request.user.id)
			if userprofiledata:
				for i in userprofiledata:
					return redirect('linkedhr:userprofile-update', i.pk) 
			else:
				#return redirect('linkedhr:login')
				return render(request, self.template_name, {'form':form})
		else:
			return redirect('linkedhr:login')

	def post(self, request):
		
		if request.user.is_authenticated():
			form = UserProfileForm(request.POST)
			if form.is_valid:
				post = form.save(commit=False)
				post.user_id = request.user
				post.save()
				sex = form.cleaned_data['sex']
				date_of_birth = form.cleaned_data['date_of_birth']
				city = form.cleaned_data['city']
				email = form.cleaned_data['email']
				phone_number = form.cleaned_data['phone_number']
				is_recruit = form.cleaned_data['is_recruit']
				description = form.cleaned_data['description']
				
				CreateStage = Stage.objects.create(user_id = request.user, stage=1, description='User profile registration.')
				CreateStage.save()
				
				#user_profile_id=CreateStage.id
				#request.session['user_profile_id'] =  user_profile_id
				
				if is_recruit == '2':
					return redirect('linkedhr:usereducation')
				else:
					return redirect('linkedhr:company')
			
			args = {'form':form, 'text':text}
			return render(request, self.template_name, args)
 
class UserProfileUpdate(generic.UpdateView):
	model = UserProfile 
	fields = ['sex', 'date_of_birth', 'city', 'email', 'phone_number', 'is_recruit', 'description'] 

## view detail of each userprofile by user_id
class UserProfileDetailTwoView(generic.ListView):
	model = UserProfile
	context_object_name = 'userprofile'
	template_name =  'userprofile/detail.html'
	
	def get_queryset(self):
		
		#if self.request.user.is_authenticated:
		if self.request.user.is_authenticated():
			try:
				userprofile_data =UserProfile.objects.filter(user_id=self.request.user.id, is_status=True)
	 			data_education = Education.objects.filter(user_id=self.request.user.id, is_status=True)
	 			data_experience = Experience.objects.filter(user_id=self.request.user.id, is_status=True)
	 			userprofile = userprofile_data,data_education, data_experience
	 			return userprofile
	 		except UserProfile.DoesNotExist:
				raise Http404(" User does not exist")
 		else:
 			return redirect('linkedhr:login') 
	

def UserProfileDetailView(request, pk=None):
	template_name =  'userprofile/detail.html'
	if pk:
		try:
			#userprofile =  UserProfile.objects.get(pk=pk, is_status=True)
			userprofile =  UserProfile.objects.filter(user_id=request.user.id, is_status=True)
			
		except UserProfile.DoesNotExist:
			raise Http404(" User does not exist")
	#else:
		#return redirect('linkedhr:login')
	args = {'userprofile':userprofile}	
	return render(request,  template_name, args) 




# ***************************************************
# ***************** BLOCK HOMEPAGE*******************
# ***************************************************
class IndexView(generic.ListView):
	template_name =  'city/index.html'
	context_object_name = 'all_city'
	paginate_by = 3
	def get_queryset(self):
		return City.objects.all();

class DetailView(generic.DetailView):
	model = City
	template_name = 'city/detail.html'

class  CityCreate(CreateView):
	model = City 
	fields = ['name', 'city_logo', 'description']

class  CityUpdate(UpdateView):
	model = City 
	fields = ['name', 'city_logo', 'description'] 

class  CityDelete(DeleteView):
	model = City 
	success_url = reverse_lazy('linkedhr:index')



# User Login from the browser for the end user 
class UserLoginView(View):
	form_class = UserLoginForm
	template_name = 'userprofile/user_login.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})	
		
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			# Cleaned (Normalize) Data
			username = form.cleaned_data['username']  
			password = form.cleaned_data['password']
			
			# return user objects if credentials are corrects 
			user = authenticate(username = username, password = password)
			if user is not None: 
				if user.is_active: 
					login(self.request, user)
					return redirect('linkedhr:index')
		return render(request, self.template_name, {'form':form})

def auth_logout(request):
  logout(request)
  return redirect('linkedhr:login')
    	
# USER Registration form and the next step is go to userprofile 
class UserFormView(View):
	form_class = UserForm
	template_name = 'city/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	# process form data
	def post(self, request):
	
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False) 
			# Cleaned (Normalize) Data
			username = form.cleaned_data['username']  
			data = User.objects.filter(username=username)

			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			# return user objects if credentials are corrects 
			user = authenticate(username = username, password = password)
			if user is not None: 
				if user.is_active: 
					login(request, user) 
					return redirect('linkedhr:userprofile') 
		return render(request, self.template_name, {'form':form}) 

		


#def index(request):
#	all_cities = City.objects.all()
#	html=''
#	for city in all_cities:
#		url = '/locations/' + str(city.id) + '/'
#		html += '<a href="'+url+'">'+ city.name + '</a><br>'
#	return HttpResponse(html)



#def index(request):
	#all_cities = City.objects.all()
	#template = loader.get_template('city/index.html')
	#context ={ 'all_city':all_cities }
	#return HttpResponse(template.render(context,request))
	#return render(request, 'city/index.html', context)
	#return render(request, 'city/index.html', { 'all_city':all_cities })

#def detail(request, location_id):
	#return HttpResponse("<h2>locations details :"+ str(location_id)+"</h2>")
	#try:
	#	city = City.objects.get(pk = location_id)
	#except City.DoesNotExist:
	#	raise Http404("City does not exist")
	
	#city = get_object_or_404(City, pk=location_id)
	#return render(request, 'city/detail.html', {'city':city})

#def blow(request, location_id):
	#city = get_object_or_404(City, pk=location_id)
	#try:
		#select_district = city.district_set.get(pk = request.POST['district'])
	#except (KeyError, District.DoesNotExist):
		#return render(request, 'locations/detail.html', {
				#'city':city,
				#'error_message': "You did not select a valid district"
			#})
	#else:
		#select_district.is_status = False
		#select_district.save()		
		#return render(request, 'city/detail.html', {'city':city})



#class IndexUserProfileView(generic.ListView):
	#template_name =  'userprofile/index.html'
	#context_object_name = 'all_user_profile'
	
	#def get_queryset(self):
		#return UserProfile.objects.filter(is_status=True)
