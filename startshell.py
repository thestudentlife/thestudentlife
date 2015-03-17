import django
django.setup()
from mainsite.models import Section, Subsection, Issue, Photo, Article, Album, FrontArticle, CarouselArticle
from workflow.models import Profile, WArticle, Revision, Review, Assignment
