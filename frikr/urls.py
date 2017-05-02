from django.conf.urls import url
from django.contrib import admin

from photos.views import home, detail
from users.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$', detail, name='photo_detail'),
    url(r'^login$', login, name='users_login'),
    url(r'^logout$', logout, name='users_logout'),
]
