from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotosQueryset


class PhotoListAPI(PhotosQueryset, ListCreateAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else self.serializer_class

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotoDetailAPI(PhotosQueryset, RetrieveUpdateDestroyAPIView):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return self.get_photos_queryset(self.request)
