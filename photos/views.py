from django.shortcuts import render

from photos.models import Photo


def home(request):
    photos = Photo.objects.all().order_by('-created_at')
    context = {
        'photos_list': photos[:5],
    }
    return render(request, 'photos/home.html', context)
