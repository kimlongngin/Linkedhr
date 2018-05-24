from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings
from linkedhr.models import City, Company

class Test(models.Model):
	
	description = models.TextField(null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_status = models.BooleanField(default=True)