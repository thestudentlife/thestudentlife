from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Section(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Subsection(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	section = models.ForeignKey(Section)
	issue= models.ForeignKey(Issue)
	subsections = models.ManyToManyField(Subsection,blank=True)
	authors = models.ManyToManyField(Author)
	published_date = models.DateTimeField(default = timezone.now)
	updated_date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.title

class FrontArticle(models.Model):
	article = models.OneToOneField(Article)
	def __str__(self):
		return self.article.title

class CarouselArticle(models.Model):
	article = models.OneToOneField(Article)
	def __str__(self):
		return self.article.title

class Author(models.Model):
	user = models.OneToOneField(User)
	def display_name(self):
		return self.user.first_name+" "+self.user.last_name
	def __str__(self): 
		return self.display_name()

class Editor(models.Model):
	user = models.OneToOneField(User)
	position = models.CharField(max_length=50)
	def display_name(self):
		return self.user.first_name+" "+self.user.last_name
	def __str__(self): 
		return self.display_name()

class Photographer(models.Model):
	user =models.OneToOneField(User)
	def display_name(self):
		return self.user.first_name+" "+self.user.last_name
	def __str__(self): 
		return self.display_name()

class Photo(models.Model):
	date = models.DateTimeField(default = timezone.now)
	image = models.ImageField(upload_to='static/uploads/')
	caption = models.TextField(max_length=500,blank=True)
	credit = models.ForeignKey(Photographer)	
	def __str__(self): 
		return self.image.url

class Album(models.Model):
	article = models.ForeignKey(Article)
	photos = model.ManyToManyField(Photo)
	def __str__(self): 
		return self.article.title

class Issue(models.Model):
	name = models.CharField(max_length=200)	















