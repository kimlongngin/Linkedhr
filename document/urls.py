from django.conf.urls import include, url
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

app_name = 'document'

urlpatterns = [
	# /linkedhr/register/userprofile/company/branch 
	#url(r'^$', views.BranchView.as_view(), name='branch'),
	#url(r'^register/userprofile/company/branch/$', views.BranchView.as_view(), name='branch'),

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
