from django.shortcuts import render

from photos.models import Photo


def home(request):
    photos = Photo.objects.all()
    context = {
        'photos_list': photos,
    }
    return render(request, 'photos/home.html', context)
