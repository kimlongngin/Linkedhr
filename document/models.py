from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings
import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

def content_file_name(instance, filename):
	#return "files/users/%s/%s" % (request.user.id, filename)
    return '/'.join(['content', instance.user.username, filename])
    
class Documents(models.Model):
	user = models.ForeignKey(User, related_name='documentuser', on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	file = models.FileField(upload_to=content_file_name, validators=[validate_file_extension])
	description = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_status = models.BooleanField(default=True)

	def __str__ (self):
		return self.title

	class Meta:
		ordering = ["-created", "-updated"]

	def get_absolute_url(self):
		return reverse('document-detail', kwargw={'pk':self.pk})

