from django.http import HttpResponse

from photos.models import Photo


def home(request):
    photos = Photo.objects.all()
    html = '<ul>'
    for photo in photos:
        html += '<li>' + photo.name + '</li>'
    html += '</ul>'
    return HttpResponse(html)
