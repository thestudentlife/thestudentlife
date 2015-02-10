from django.db import models
from django.contrib.auth.models import User
from mainsite.models import Article,Editor
from django.utils import timezone
# Create your models here.

class WProfile(models.Model):
	user = models.OneToOneField(User,related_name="profile")
	POSITIONS_CHOICES= (
		('ChiefEditor','Chief Editor'),
		('CopyEditor','Copy Editor'),
		)
	position = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES,default='Editor')
	def is_author():
		return self.user.author != None
	def is_photographer():
		return self.user.photographer != None
	def is_editor():
		return self.editor != None
	def display_name(self):
		return self.user.first_name+" "+self.user.last_name

class WArticle(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.OneToOneField(Article)
	status = models.TextField()
	locker = models.ForeignKey(User,blank=True)
	def locked(self):
		return self.locker != None
	def __str__(self):
		return self.article.title

class WReview(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.ForeignKey(Article)
	reviewer = models.CharField(max_length=50)
	comment = models.TextField(blank=True)

class WRevision(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.ForeignKey(Article)
	editor = models.ForeignKey(Editor)
	body = models.TextField()






