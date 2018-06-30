from django.conf.urls import include, url
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib import admin


app_name = 'chat'

urlpatterns = [
	# /chat/

	url(r'^$', views.home, name='chatindex'),
	url(r'^chat/$', views.chat, name='chat'),

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
