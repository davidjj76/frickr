from django.conf.urls import url
from django.contrib import admin

from photos.api import PhotoListAPI
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView
from users.views import LoginView, LogoutView

from users.api import UserListAPI, UserDetailAPI

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Photos
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^my-photos/$', UserPhotosView.as_view(), name='user_photos'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_list'),
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
    url(r'^photos/new$', CreateView.as_view(), name='photo_create'),

    # Users
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    # Users API
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='users_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),

    # Photos API
    url(r'^api/1.0/photos/$', PhotoListAPI.as_view(), name='photo_list_api'),

]
