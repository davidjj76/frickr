from django.conf.urls import url
from django.contrib import admin

from photos.views import home, detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^photos/(?P<pk>[0-9]+)$', detail),
]
