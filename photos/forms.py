from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ('owner',)

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError('La palabra {0} no está permitida'.format(badword))

        return cleaned_data
