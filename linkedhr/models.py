from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings

# Create your models here.

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %(instance.id, instance.id, extension)

class City(models.Model):
	name = models.CharField(max_length=100)
	city_logo = models.FileField()
	#city_logo = models.ImageField(upload_to = upload_location,
				#null=True, blank=True,
				#width_field="width_field",
				#height_field="height_field"
				#)
	#width_field = models.IntegerField(default=0)
	#height_field = models.IntegerField(default=0)
	description = models.TextField(null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_status = models.BooleanField(default=True)
	
	def get_absolute_url(self):
		return reverse('linkedhr:detail', kwargs={'pk':self.pk})
	
	def __str__ (self):
		return self.name
	
	class Meta:
		ordering = ["-created", "-updated"]
						
class District(models.Model):
	name = models.CharField(max_length=100)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	description = models.TextField()
	is_status = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
		return self.name +' - '+ self.description	

class Villege(models.Model):
	name = models.CharField(max_length=100)
	district = models.ForeignKey(District, on_delete=models.CASCADE)
	description = models.TextField()
	is_status = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
			return self.name +' - '+ self.description
	class Meta:
		ordering = ["-created", "-updated"]

class Stage(models.Model):
	user_id = models.ForeignKey(User, related_name='stageuserprofile', on_delete=models.CASCADE)
	stage = models.CharField(max_length=4)
	description = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_status = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('stage-detail', kwargw={'pk':self.pk})

	class Meta:
		ordering = ["-created", "-updated", "-user_id"]



# Userprofile has two basic by one is recruitor and other one is job_applyer 

IS_RECRUITE = (
    ('1', 'Recruiter'),
    ('2', 'Seeker'),
)
class UserProfile(models.Model):

	user_id = models.OneToOneField(User, related_name='profile')
	sex = models.CharField(max_length=3, choices=TITLE_CHOICES)
	date_of_birth =  models.DateField(auto_now=False, default=date.today, blank=True)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20)
	is_recruit = models.CharField(max_length=10, choices=IS_RECRUITE, verbose_name='What will you do ?')
	description= models.TextField()
	is_status = models.BooleanField(default=True)
	authority = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	
	def get_absolute_url(self):
		return reverse('linkedhr:detail', kwargs={'pk':self.pk})
	
	class Meta:
		ordering = ["-created", "-updated"]

# Company that work for upload their jobs, company has relationship with table branch, jobs 
class Company(models.Model):
	user_id = models.ForeignKey(User, related_name='user_company', on_delete=models.CASCADE)
	name = models.CharField(max_length=150)
	company_logo = models.FileField()
	email = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=30)
	#google_map = models.CharField(max_length=150)
	location = models.ForeignKey(City, on_delete=models.CASCADE)
	address = models.CharField(max_length=150)
	web_site = models.CharField(max_length=150)
	description = models.TextField()
	is_status = models.BooleanField(default=False)
	is_branch = models.BooleanField(default=False, verbose_name='Does your company has more than one branch ?')
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)

	def get_absolute_url(self):
		return reverse('linkedhr:detail', kwargs={'pk':self.pk})
	
	def __str__ (self):
		return self.name

	class Meta:
		ordering = ["-created", "-updated"]


# Brand has relationship with locations and company table 
class Branch(models.Model):
	company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	location = models.ForeignKey(City, on_delete=models.CASCADE)
	address = models.CharField(max_length=150)
	web_site = models.CharField(max_length=150)
	email = models.EmailField(max_length=250)
	phone_number = models.CharField(max_length=50)
	description = models.TextField()
	is_status = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
		return self.is_status
	class Meta:
		ordering = ["-created", "-updated"]

#  Degree Has relationship with user one-many  
IS_DEGREE = (
    ('1', 'POS_DOC'),
    ('2', 'PHD'),
    ('3', 'MS'),
    ('4', 'BC'),
    ('5', 'Other'),
)
class Education(models.Model):
	user_id = models.ForeignKey(User, related_name='user_education', on_delete=models.CASCADE)
	majority = models.CharField(max_length=150)
	degree = models.CharField(max_length=10, choices=IS_DEGREE, verbose_name='Degree')
	institute = models.CharField(max_length=150)
	start_education_at = models.DateField(auto_now=False, default=date.today, blank=True, verbose_name='Start at')
	graduation_at = models.DateField(auto_now=False, default=date.today, blank=True, verbose_name='Graduation at')
	description = models.TextField()
	is_status = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	
	class Meta:
		ordering = ["-created", "-updated"]

# Create model Skill category, has relationship with Skill in many-one
class SkillList(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	is_status = models.BooleanField(default=True)	
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
		return self.is_status
	class Meta:
		ordering = ["-created", "-updated"]

# Skill has relationship with SkillList in one-many
class Skill(models.Model):
	user_id = models.IntegerField(default=0)
	title = models.CharField(max_length=100)
	skill_list = models.ForeignKey(SkillList, on_delete=models.CASCADE)
	description = models.TextField()
	is_status = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
		return self.is_status
	class Meta:
		ordering = ["-created", "-updated"]

class Document(models.Model):
	user_id = models.ForeignKey(UserProfile, related_name='user_document')
	name = models.CharField(max_length=100)
	document = models.FileField()
	description = models.TextField()
	is_status = models.BooleanField(default=True)
		
class ExperienceCheck(models.Model):
	user_id = models.ForeignKey(User, related_name='experience_user')
	is_experience = models.BooleanField(default=False)
	

# Experience of student or employee that has work before 
class Experience(models.Model):
	user_id = models.ForeignKey(User, related_name='user_experience', on_delete=models.CASCADE)
	position = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	start_date =models.DateField(auto_now=False, default=date.today, blank=True)
	due_date = models.DateField(auto_now=False, default=date.today, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	description = models.TextField()
	is_status = models.BooleanField(default=False)
	
	class Meta:
		ordering = ["-created", "-updated"]

# Job position for each companies 
class Position(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	is_status = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	
	def __str__ (self):
		return self.name
	class Meta:
		ordering = ["-created", "-updated"]

# Jobtype has vip, urgent, new 		
class JobType(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	is_status = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
		return self.is_status
	class Meta:
		ordering = ["-created", "-updated"]

class RecruitmentBranch(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
		return self.is_status
	class Meta:
		ordering = ["-created", "-updated"]

# job has relationship with jobtype in OneToOne
class Recruitment(models.Model):
	user_id = models.IntegerField(default=0)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	position = models.ForeignKey(Position, on_delete=models.CASCADE)
	Branch = models.ForeignKey(RecruitmentBranch, on_delete=models.CASCADE)
	salary = models.CharField(max_length=30)
	number_of_employee = models.IntegerField(default=0)
	experience = models.CharField(max_length=30)
	start_date =models.DateField(auto_now=False, default=date.today, blank=True)
	due_date = models.DateField(auto_now=False, default=date.today, blank=True)
	job_requirement = models.TextField()
	email = models.EmailField(max_length=250)
	phone_number = models.CharField(max_length=20)
	address = models.CharField(max_length=150)
	job_type = models.OneToOneField(
        JobType,
        on_delete=models.CASCADE,
        related_name='jobtype_of',
    )
	is_status = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__ (self):
		return self.is_status
	class Meta:
		ordering = ["-created", "-updated"]

class Apply(models.Model):
	user_id = models.IntegerField(default=0)
	position = models.ForeignKey(Recruitment, on_delete=models.CASCADE)
	stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
	description = models.TextField()	
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_status = models.BooleanField(default=False)
	def __str__ (self):
		return self.is_status
	class Meta:
		ordering = ["-created", "-updated"]