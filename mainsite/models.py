from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm, Textarea, TextInput
from django.template.defaultfilters import slugify
from workflow.models import Profile

class Section(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Subsection(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Issue(models.Model):
	name = models.CharField(max_length=200)	

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	section = models.ForeignKey(Section,related_name='articles')
	issue= models.ForeignKey(Issue)
	subsections = models.ManyToManyField(Subsection,null=True)
	authors = models.ManyToManyField(Profile)
	published_date = models.DateTimeField(default = timezone.now)
	updated_date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.title
	def slug(self):
		return slugify(self.title)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','section','subsections']
        widgets = {
		'title':TextInput(attrs={
			'required':True
			}),
		'content':Textarea(attrs={
			'required':True
			}),
		}


class FrontArticle(models.Model):
	article = models.OneToOneField(Article)
	def __str__(self):
		return self.article.title

class CarouselArticle(models.Model):
	article = models.OneToOneField(Article)
	def __str__(self):
		return self.article.title


class Photo(models.Model):
	date = models.DateTimeField(default = timezone.now)
	image = models.ImageField(upload_to='media/uploads/')
	caption = models.TextField(max_length=500,blank=True)
	credit = models.ForeignKey(Profile)	
	def __str__(self): 
		return self.image.url

class Album(models.Model):
	article = models.ForeignKey(Article)
	photos = models.ManyToManyField(Photo)
	def __str__(self): 
		return self.article.title
















