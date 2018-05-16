from django.conf.urls import include, url
from django.contrib import admin
from django.apps import apps

urlpatterns = [
	#url(r'^locations/', include('locations.urls', namespace='locations')),
	#url('<int:question_id>/', views.detail, name='detail'),
	url(r'^linkedhr/', include('linkedhr.urls', namespace='linkedhr')),
	url(r'^admin/', include(admin.site.urls)),
]
