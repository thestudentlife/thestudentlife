from django.db import models
from django.contrib.auth.models import User
from mainsite.models import Article,Editor
from django.utils import timezone
# Create your models here.

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






