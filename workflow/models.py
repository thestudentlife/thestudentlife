from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm,EmailInput,TextInput,Textarea,PasswordInput
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(User)
    POSITIONS_CHOICES= (
        ('chief_editor','Chief Editor'),
        ('copy_editor','Copy Editor'),
        ('photographer','Photographer'),
        ('author','Author'),
        ('graphic_designer','Graphic Designer'),
        ('web_developer','Web Developer'),
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
    article = models.OneToOneField('mainsite.Article')
    status = models.TextField()
    locker = models.ForeignKey(User,blank=True)
    def locked(self):
        return self.locker.exists()
    def __str__(self):
        return self.article.title

class Review(models.Model):
    date = models.DateTimeField(default = timezone.now)
    article = models.ForeignKey('mainsite.Article')
    reviewer = models.CharField(max_length=50)
    comment = models.TextField(blank=True)

class Revision(models.Model):
    date = models.DateTimeField(default = timezone.now)
    article = models.ForeignKey('mainsite.Article')
    editor = models.ForeignKey(Profile)
    body = models.TextField()

class Assignment(models.Model):
    TYPES_CHOICES = (
        ('photo_assignment','Photo Assignment'),
        ('article_assignment','Article Assignment')
    )
    sender = models.ForeignKey(Profile,related_name="assignment_created")
    receiver = models.ForeignKey(Profile,default=None,related_name="assignment_received")
    title = models.CharField(max_length=200)
    type = models.CharField(choices=TYPES_CHOICES,max_length=50,default='photo_assignment')
    content = models.TextField(blank=True)
    section = models.ForeignKey('mainsite.Section')
    created_date = models.DateTimeField(default = timezone.now)
    due_date = models.DateTimeField(default = timezone.now)
    response_article = models.ForeignKey('mainsite.Article',related_name="assignment",null=True)
    response_photo = models.ForeignKey('mainsite.Photo',related_name="assignment",null=True)
    def progress(self):
        if self.response_article is not None or self.response_photo is not None:
            return "finished"
        elif self.receiver is not None:
            return "in progress"
        else:
            return "not started"
    def __str__(self):
        return self.title

class AssignmentForm(models.Model):
    class meta:
        fields = ['title','content','section','type','due_date']

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
        'password': PasswordInput(attrs={
            'required':True
            }),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['position']







