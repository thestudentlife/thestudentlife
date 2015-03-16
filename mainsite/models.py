from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm, Textarea, TextInput
from django.template.defaultfilters import slugify
from django.views.generic import CreateView
from workflow.models import Profile, Assignment, WArticle
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from workflow.models import Profile, Assignment, WArticle, Revision

class Section(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('section',kwargs={'section_name':self.name})

class Subsection(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('section',kwargs={'section_name':self.name})

class Issue(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('issue',kwargs={'issue_id':self.id})

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    section = models.ForeignKey(Section, related_name='articles')
    issue = models.ForeignKey(Issue)
    authors = models.ManyToManyField(Profile)
    subsections = models.ManyToManyField(Subsection, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    def has_photo(self):
        return self.albums.photos is not None
    def slug(self):
        return slugify(self.title)
    def get_absolute_url(self):
        return reverse('article',kwargs={'article_id':self.id,'section_name':self.section.name})

class FrontArticle(models.Model):
    article = models.OneToOneField(Article)

    def __str__(self):
        return self.article.title

class CarouselArticle(models.Model):
    article = models.OneToOneField(Article)

    def __str__(self):
        return self.article.title

class Photo(models.Model):
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photo/')
    caption = models.TextField(max_length=500, blank=True)
    credit = models.ForeignKey(Profile)

    def __str__(self):
        return self.image.url

class Album(models.Model):
    article = models.OneToOneField(Article)
    photos = models.ManyToManyField(Photo,null=True)
    def __str__(self):
        return self.article.title

# The assignment form is currently in the mainsite
# because of a circular dependency on Section.
# Ideally, this class should be moved back to workflow/models.
class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['title','content','section','type','receiver','due_date']
        widgets = {
            'due_date': TextInput(attrs={
                'type': 'date',
            })
        }













