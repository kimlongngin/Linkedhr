from django.conf.urls import include, url
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

app_name = 'linkedhr'

urlpatterns = [

	# /linkedhr/
	url(r'^$', views.IndexView.as_view(), name='index'),
	
	# /linkedhr/register
	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	# /linkedhr/register/userprofile 
	url(r'^register/userprofile/$', views.UserProfileView.as_view(), name='userprofile'),
	
	#url(r'^register/myuserprofile/(?P<user_id>\d+)/$', views.UserProfileDetailView.as_view(), name='myuserprofile_with_pk'),
	url(r'^register/myuserprofile/(?P<pk>[0-9]+)/$', views.UserProfileDetailView, name='myuserprofile_with_pk'),

	#url(r'^register/myuserprofile/(?P<user_id>\d+)/$', views.UserProfileDetailView.as_view(), name='myuserprofile_with_pk'),
	url(r'^register/detailuserprofile/$', views.UserProfileDetailTwoView.as_view(), name='myuserprofile_without_pk'),
	
	# /linkedhr/register/userprofile/userprofileupdate/1
    url(r'register/userprofile/userprofileupdate/(?P<pk>[0-9]+)/$', views.UserProfileUpdate.as_view(), name='userprofile-update'),

	# /linkedhr/register/userprofile/usereducation 
	url(r'^register/userprofile/usereducation/$', views.EducationView.as_view(), name='usereducation'),
	
	# /linkedhr/register/userprofile/usereducation/1
    url(r'^register/userprofile/updateeducation(?P<pk>[0-9]+)/$', views.EducationUpdate.as_view(), name='education-update'),

	# /linkedhr/register/userprofile/userexperience 
	url(r'^register/userprofile/userexperience/$', views.ExperienceView.as_view(), name='userexperience'),

	# /linkedhr/register/userprofile/usereducation/1
    url(r'^register/userprofile/experienceupdate(?P<pk>[0-9]+)/$', views.ExperienceUpdate.as_view(), name='experience-update'),

	# /linkedhr/register/userprofile/company 
	url(r'^register/userprofile/company/$', views.CompanyView.as_view(), name='company'),

	# /linkedhr/register/userprofile/company/branch 
	url(r'^register/userprofile/company/branch/$', views.BranchView.as_view(), name='branch'),


	# /linkedhr/register/userprofile/company/1 
	url(r'register/userprofile/company/(?P<pk>[0-9]+)/$', views.CompanyUpdateView.as_view(), name='company-update'),
	
	# /linkedhr/register/userprofile/company/list_company
	url(r'^register/userprofile/company/list_company/(?P<pk>[0-9]+)/$', views.ListCompanyView.as_view(), name='list_company'),

	# /linkedhr/login
	#url(r'^login/$', auth_views.login, name='login'),
	url(r'^login/$', auth_views.login, name='login'),
	
	#url(r'^logout/$', auth_views.logout, name = 'logout'),
	url(r'^logout/$', views.auth_logout, name='auth_logout' ),
	# /linkedhr/<city_id>
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	
	# /linkedhr/city/add
    url(r'city/add/$', views.CityCreate.as_view(), name='city-add'),
    # /linkedhr/city/2
    url(r'city/(?P<pk>[0-9]+)/$', views.CityUpdate.as_view(), name='city-update'),

	# /linkedhr/city/2/delete
    url(r'city/(?P<pk>[0-9]+)/delete$', views.CityDelete.as_view(), name='city-delete'),

    # /linkedhr/
    #url(r'^$', views.index, name='index'),
   	
   	   	# /linkedhr/<city_id>
    #url(r'^(?P<location_id>[0-9]+)/$', views.detail, name='detail'),
    # /linkedhr/<city_id>
    #url(r'^(?P<location_id>[0-9]+)/blow/$', views.blow, name='blow'),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
