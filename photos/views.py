from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5],
    }
    return render(request, 'photos/home.html', context)


def detail(request, pk):
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto!!!')


def create(request):
    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST)
        if form.is_valid():
            new_photo = form.save()
            form = PhotoForm()
            success_message = 'Guardado con éxito! '
            success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += 'Ver foto'
            success_message += '</a>'
    context = {
        'form': form,
        'success_message': success_message,
    }
    return render(request, 'photos/new_photo.html', context)
