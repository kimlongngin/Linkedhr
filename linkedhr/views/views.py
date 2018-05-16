from django.shortcuts import render, get_object_or_404
from django.template import loader 
from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
# For user registration
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login 
from django.views.generic import View 

from .models import City
from .forms import UserForm, UserLoginForm
 

class IndexView(generic.ListView):
	template_name =  'city/index.html'
	context_object_name = 'all_city'
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
    	email = request.post['email']
    	password = request.POST['password']
    	user = authenticate(email=email, password=password)
    	if user is not None:
    		if user.is_active:
        		login(request, user)
        		return redirect('www.komlang.com')
        	else 
        		return 'User is inactive'
        else:
        	return redirect('www.baidu.com')

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
			username = form.clean_data['username']  
			password = form.clean_data['password']
			user.set_password(password)
			user.save()
			# return user objects if credentials are corrects 
			user = authenticate(username = username, password = password)
			if user is not None: 
				if user.is_active: 
					login(request, user)
					return redirect('linkedhr:index')
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