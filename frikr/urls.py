from django.conf.urls import url
from django.contrib import admin

from photos.views import HomeView, detail, create
from users.views import LoginView, LogoutView

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Photos
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$', detail, name='photo_detail'),
    url(r'^photos/new$', create, name='photo_create'),

    # Users
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
]
