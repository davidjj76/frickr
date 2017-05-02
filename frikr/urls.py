from django.conf.urls import url
from django.contrib import admin

from photos.views import home, detail, create
from users.views import login, logout

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Photos
    url(r'^$', home, name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$', detail, name='photo_detail'),
    url(r'^photos/new$', create, name='photo_create'),

    # Users
    url(r'^login$', login, name='users_login'),
    url(r'^logout$', logout, name='users_logout'),
]
