from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings


def content_file_name(instance, filename):
	#return "files/users/%s/%s" % (request.user.id, filename)
    return '/'.join(['content', instance.user.username, filename])
    
class Documents(models.Model):
	user = models.ForeignKey(User, related_name='documentuser', on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	file = models.FileField(upload_to=content_file_name)
	description = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_status = models.BooleanField(default=True)

	class Meta:
		ordering = ["-created", "-updated"]

	def get_absolute_url(self):
		return reverse('document-detail', kwargw={'pk':self.pk})

