from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ('owner',)

