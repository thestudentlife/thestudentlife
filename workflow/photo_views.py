from django.forms import inlineformset_factory, ModelForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from mainsite.models import Album, Photo, Issue
from workflow.views import group_required

# photos
@group_required('silver')
def photos(request):
    return HttpResponse('These are the photos.')

@group_required('bronze')
def photo(request, photo_id):
    return HttpResponse('This is photo ' + str(photo_id))

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']

@group_required('bronze')
def edit_photo(request, photo_id):
    return HttpResponse('You are going to edit photo ' + str(photo_id))

@group_required('bronze')
def albums(request):
    issues = Issue.objects.order_by('-created_date')
    return render(request, 'photo/albums.html', {'issues': issues})

@group_required('bronze')
def issue_albums(request, issue_id):
    issue = Issue.objects.get(pk=issue_id)
    albums = Album.objects.all()
    filtered_albums = []
    for album in albums:
        if (issue_id == str(album.article.issue.pk)):
            filtered_albums.append(album)
    return render(request, 'photo/issue_albums.html', {'albums': filtered_albums, 'issue': issue})

@group_required('silver')
def view_album(request, issue_id, album_id):
    issue = Issue.objects.get(pk=issue_id)
    album = Album.objects.get(pk=album_id)
    return render(request, 'photo/view_album.html', {'album': album, 'issue': issue})

@group_required('silver')
def edit_album(request, issue_id, album_id):
    album = Album.objects.get(pk=album_id)
    PhotoInlineFormSet = inlineformset_factory(Album, Photo, form=PhotoForm)
    if request.method == "POST":
        formset = PhotoInlineFormSet(request.POST, request.FILES, instance=album)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.credit = request.user.profile
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            formset.save_m2m()
            return HttpResponse("Success!")
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