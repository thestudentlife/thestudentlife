from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm,EmailInput,TextInput,Textarea,PasswordInput
from django.template.defaultfilters import slugify
from mainsite.models import Article,Section,Photo

class Profile(models.Model):
	user = models.OneToOneField(User)
	POSITIONS_CHOICES= (
		('chief_editor','Chief Editor'),
		('copy_editor','Copy Editor'),
		('photographer','Photographer'),
		('author','Author'),
		('graphic_designer','Graphic Designer')
		)
	position = models.CharField(choices=POSITIONS_CHOICES,max_length=50,default='Editor')
	def slug(self):
		return slugify(self.get_profile().display_name())
	def display_name(self):
		return self.user.first_name+" "+self.user.last_name
	def __str__(self): 
		return self.display_name()+"'profile"

class WArticle(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.OneToOneField(Article)
	status = models.TextField()
	locker = models.ForeignKey(User,blank=True)
	def locked(self):
		return self.locker.exists()
	def __str__(self):
		return self.article.title

class Review(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.ForeignKey(Article)
	reviewer = models.CharField(max_length=50)
	comment = models.TextField(blank=True)

class Revision(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.ForeignKey(Article)
	editor = models.ForeignKey(Profile)
	body = models.TextField()

class Assignment(models.Model):
	sender = models.ForeignKey(Profile)
	receiver = models.ForeignKey(Profile,default=None)
	title = models.CharField(max_length=200)
	content = models.TextField()
	section = models.ForeignKey(Section)
	created_date = models.DateTimeField(default = timezone.now)
	due_date = models.DateTimeField()

class Article_Assignment(Assignment):
	article = models.ForeignKey(Article,default=None)
	def is_article(self):
		return True
	def finished(self):
		self.article.exists()

class Photo_assignment(Assignment):
	photo = models.ForeignKey(Photo,default=None)
	def finished(self):
		self.photo.exists()
	def is_article(self):
		return False

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		widgets = {
		'username':TextInput(attrs={
			'required':True
			}),
		'password':PasswordInput(attrs={
			'required':True
			})		
		} 

class RegisterForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']
		widgets = {
		'email':EmailInput(attrs={
			'required':True
			}),
		'first_name':TextInput(attrs={
			'required':True
			}),
		'last_name':TextInput(attrs={
			'required':True
			}),
		'password': PasswordInput()		
		}





