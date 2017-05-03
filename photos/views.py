from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


class PhotosQueryset(object):

    def get_photos_queryset(self, request):
        if not request.user.is_authenticated():
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos


class HomeView(View):

    def get(self, request):
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            'photos_list': photos[:5],
        }
        return render(request, 'photos/home.html', context)


class DetailView(View, PhotosQueryset):

    def get(self, request, pk):
        possible_photos = self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
        photo = possible_photos[0] if len(possible_photos) == 1 else None
        if photo is not None:
            context = {
                'photo': photo
            }
            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('No existe la foto!!!')


class CreateView(View):

    @method_decorator(login_required())
    def get(self, request):
        form = PhotoForm()
        context = {
            'form': form,
            'success_message': '',
        }
        return render(request, 'photos/new_photo.html', context)


    @method_decorator(login_required())
    def post(self, request):
        success_message = ''
        photo_with_owner = Photo(owner=request.user)
        form = PhotoForm(request.POST, instance=photo_with_owner)
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


class ListView(View, PhotosQueryset):

    def get(self, request):
        context = {
            'photos': self.get_photos_queryset(request),
        }
        return render(request, 'photos/list.html', context)
