from django.core.exceptions import ValidationError


def validate_file_extension(value):
    if value.file.content_type != 'text/plain':
        raise ValidationError(u'Wrong file extension')
