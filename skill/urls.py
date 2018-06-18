from django.conf.urls import include, url
from django.contrib import admin
from django.apps import apps

urlpatterns = [
	url(r'^skill/', include('skill.urls')),
	url(r'^linkedhr/', include('linkedhr.urls', namespace='linkedhr')),
	url(r'^admin/', include(admin.site.urls)),
]