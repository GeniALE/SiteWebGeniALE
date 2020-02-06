from django.db.models import ManyToManyField
from django.db.models.fields.files import ImageField


def to_dict(instance, extra_fields=[]):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
        elif isinstance(f, ImageField):
            # We have to convert the value to a string to erase the "ImageField" type.
            data[f.name] = str(f.value_from_object(instance))
        else:
            data[f.name] = f.value_from_object(instance)
    for f in extra_fields:
        if hasattr(instance, f):
            data[f] = getattr(instance, f)

    return data
