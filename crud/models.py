from distutils.command.install import install

from django.db import models

# Create your models here.
from django.utils import timezone


def full_path(instance, filename):
    if isinstance(instance, Person):
        # file will be uploaded to MEDIA_ROOT/person/picture/<filename>
        return f'person/picture/{filename}'
    elif isinstance(instance, ImageCatalog):
        # file will be uploaded to MEDIA_ROOT/person/78/<filename>
        return f'person/{instance.person.id}/{filename}'


class Person(models.Model):
    picture = models.FileField(upload_to=full_path, default='person/picture/profile.jpg')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(default='')
    is_active = models.BooleanField(default=True)
    date_update = models.DateTimeField(auto_now=timezone.now())
    date_joined = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return f'ID {self.id} - Nombre: {self.first_name} {self.last_name}'


class ImageCatalog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.FileField(upload_to=full_path)
    date_joined = models.DateTimeField(auto_now_add=timezone.now())
