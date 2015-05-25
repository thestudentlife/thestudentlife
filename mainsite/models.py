import autocomplete_light
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm, TextInput
from django.template.defaultfilters import slugify
from workflow.models import Profile, Assignment, WArticle
from django.core.urlresolvers import reverse, reverse_lazy
from workflow.models import Profile, Assignment, WArticle, Revision
import re
autocomplete_light.autodiscover()

class Section(models.Model):
    name = models.CharField(max_length=50)
    priority = models.IntegerField(blank=True, null=True)
    legacy_id = models.PositiveIntegerField(blank=True, null=True)
    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return reverse('section', kwargs={'section_slug': self.slug()})

class Subsection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'section_name': self.name})

class Issue(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    legacy_id = models.IntegerField(null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('issue', kwargs={'issue_id': self.id})

class Copy(models.Model):
    created_date = models.DateTimeField(default=datetime.datetime.now)
    file = models.FileField(upload_to='archives/')
    def __str__(self):
        return self.file.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    section = models.ForeignKey(Section, related_name='articles')
    issue = models.ForeignKey(Issue)
    authors = models.ManyToManyField(Profile)
    clicks = models.IntegerField(default=0)
    subsections = models.ManyToManyField(Subsection, null=True)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(default=datetime.datetime.now)
    legacy_id = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title

    def content_with_no_images(self):
        return re.sub("<img[^>]*>","", re.sub("<a[^>]*>","", self.content));

    def has_photo(self):
        return self.album.photo_set is not None

    def disqus_id(self):
        if self.legacy_id:
            return "aardvark_"+str(self.legacy_id)
        else:
            return 'wolverine_'+str(self.id)

    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.id, 'section_name': self.section.slug()})

    def click(self):
        self.clicks += 1

class FrontArticle(models.Model):
    article = models.OneToOneField(Article)

    def __str__(self):
        return self.article.title

class CarouselArticle(models.Model):
    article = models.OneToOneField(Article)

    def __str__(self):
        return self.article.title

class Album(models.Model):
    article = models.OneToOneField(Article)

    def __str__(self):
        return self.article.title

class Photo(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    image = models.ImageField(upload_to='photo/')
    thumbnail = models.ImageField(upload_to='thumbs/',blank=True,null=True)
    caption = models.TextField(max_length=100, blank=True)
    credit = models.ForeignKey(Profile)
    album = models.ForeignKey(Album, null=True)

    # Adapted from http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/
    def create_thumbnail(self):

        if not self.image:
            return

        from io import BytesIO
        from PIL import Image
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os

        THUMBNAIL_SIZE = (300,300)

        DJANGO_TYPE = self.image.file.content_type
        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        r = BytesIO(self.image.read())
        fullsize_image = Image.open(r)
        image = fullsize_image.copy()

        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = BytesIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into ImageField
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('{}_thumbnail.{}'.format(os.path.splitext(suf.name)[0], FILE_EXTENSION), suf, save=False)


    def save(self):
        self.thumbnail.delete()
        self.create_thumbnail()
        super(Photo, self).save()

    def __str__(self):
        return self.image.url

# The assignment form is currently in the mainsite
# because of a circular dependency on Section.
# Ideally, this class should be moved back to workflow/models.
class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'content', 'section', 'type', 'receiver', 'due_date']
        widgets = {
            'due_date': TextInput(attrs={
                'type': 'date',
            })
        }

class ArticleForm(autocomplete_light.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'section', 'issue','authors']
        autocomplete_fields = ('authors')








