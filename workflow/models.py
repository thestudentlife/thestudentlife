from django.db import models
from django.contrib.auth.models import User, Group
import datetime
from django.forms import ModelForm, EmailInput, TextInput, Textarea, PasswordInput, CharField, DateField
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse, reverse_lazy

class Profile(models.Model):
    user = models.OneToOneField(User,null=True)
    POSITIONS_CHOICES = (
        ('chief_editor', 'Editor-in-Chief'),
        ('administrator', 'Administrator'),
        ('web_developer', 'Web Developer'),
        ('editor', 'Section Editor'),
        ('author', 'Author'),
        ('guest', 'Guest Author'),
        ('photographer', 'Photographer'),
        ('graphic_designer', 'Graphic Designer'),
    )
    position = models.CharField(choices=POSITIONS_CHOICES, max_length=50, default='author')
    display_name = models.CharField(blank=True,max_length=50)
    legacy_id = models.PositiveIntegerField(null=True)

    def slug(self):
        return slugify(self.display_name)

    def __str__(self):
        return self.display_name

    def num_assignments(self):
        assignments = self.assignment_received.all().filter(accepted=False)
        return len(assignments)

    def ideal_group_names(self):
        if self.position == 'chief_editor' or self.position == 'web_developer' or self.position == 'administrator':
            return ['gold','silver','bronze','plastic']
        elif self.position == 'editor':
            return ['silver','bronze','plastic']
        elif self.position == 'photographer' or self.position == 'author':
            return ['bronze','plastic']
        else:
            return ['plastic']

    def get_absolute_url(self):
        return reverse('person', kwargs={'person_id': self.id})

class WArticle(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    article = models.OneToOneField('mainsite.Article')
    status = models.TextField()

    def __str__(self):
        return self.article.title

    def get_absolute_url(self):
        return reverse('warticle', kwargs={'issue_id': self.article.issue.id, 'pk': self.article.id})

class Revision(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    article = models.ForeignKey('mainsite.Article')
    editor = models.ForeignKey(Profile)
    body = models.TextField()

    def __str__(self):
        return str(self.date)

class Comment(models.Model):
    article = models.ForeignKey('mainsite.Article')
    body = models.TextField()
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(default=datetime.datetime.now)

class Review(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    article = models.ForeignKey('mainsite.Article')
    reviewer = models.CharField(max_length=50)
    comment = models.TextField(blank=True)

class Assignment(models.Model):
    TYPES_CHOICES = (
        ('photo', 'Photo Assignment'),
        ('article', 'Article Assignment')
    )
    sender = models.ForeignKey(Profile, related_name="assignment_created")
    receiver = models.ForeignKey(Profile, related_name="assignment_received", null=True)
    title = models.CharField(max_length=200)
    type = models.CharField(choices=TYPES_CHOICES, max_length=50, default='photo_assignment')
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    accepted = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    response_article = models.ForeignKey('mainsite.Article', related_name="assignment", null=True)
    response_photo = models.ForeignKey('mainsite.Photo', related_name="assignment", null=True)

    def progress(self):
        if self.finished:
            return "Finished"
        elif self.accepted:
            return "In Progress"
        else:
            return "Not Started"

    def progress_status(self):
        if self.finished:
            return 0
        elif self.accepted:
            return 1
        else:
            return 2

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assignment', kwargs={'assignment_id': self.id})

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'required': True
            }),
            'password': PasswordInput(attrs={
                'required': True
            })
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'email': EmailInput(attrs={
                'required': True
            }),
            'first_name': TextInput(attrs={
                'required': True
            }),
            'last_name': TextInput(attrs={
                'required': True
            }),
            'password': PasswordInput(attrs={
                'required': True
            }),
        }

class RegisterForm2(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'email': EmailInput(attrs={
                'required': True
            })
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name','position']


