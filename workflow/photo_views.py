from django.forms import inlineformset_factory, ModelForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from mainsite.models import Album, Photo, Issue
from workflow.views import group_required
import autocomplete_light

autocomplete_light.autodiscover()

class PhotoForm(autocomplete_light.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption', 'credit']
        autocomplete_fields = ('credit')

@group_required('silver')
def edit_photo(request, photo_id):
    return HttpResponse('You are going to edit photo ' + str(photo_id))

@group_required('silver')
def albums(request):
    issues = Issue.objects.order_by('-created_date')
    return render(request, 'photo/albums.html', {'issues': issues})

@group_required('silver')
def issue_albums(request, issue_id):
    issue = Issue.objects.get(pk=issue_id)
    albums = Album.objects.filter(article__issue__pk=issue_id)
    return render(request, 'photo/issue_albums.html', {'albums': albums, 'issue': issue})

@group_required('silver')
def view_album(request, issue_id, album_id):
    issue = Issue.objects.get(pk=issue_id)
    album = Album.objects.get(pk=album_id)
    return render(request, 'photo/view_album.html', {'album': album, 'issue': issue})

@group_required('silver')
def edit_album(request, issue_id, album_id):
    album = Album.objects.get(pk=album_id)
    issue = Issue.objects.get(pk=issue_id)
    PhotoInlineFormSet = inlineformset_factory(Album, Photo, form=PhotoForm)
    if request.method == "POST":
        formset = PhotoInlineFormSet(request.POST, request.FILES, instance=album)
        if formset.is_valid():
            formset.save()
            return render(request, 'photo/view_album.html', {'album': album, 'issue': issue})
    else:
        formset = PhotoInlineFormSet(instance=album)
    return render_to_response("photo/edit_album.html", RequestContext(request, {
        "formset": formset
    }))

@group_required('silver')
def select_photos(request, issue_id, album_id):
    issue = Issue.objects.get(pk=issue_id)
    album = Album.objects.get(pk=album_id)
    return render(request, 'photo/image_selector.html', {'album': album, 'issue': issue})