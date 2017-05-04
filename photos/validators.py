from django.core.exceptions import ValidationError

from photos.settings import BADWORDS


def badwords_detector(value):
    # en python 2
    # cleaned_data = super(PhotoForm, self).clean()
    # en python 3
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError('La palabra {0} no está permitida'.format(badword))

    return True
