from django.db import models

# Create your models here.
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(default='')
    is_active = models.BooleanField(default=True)
    date_update = models.DateTimeField(auto_now=timezone.now())
    date_joined = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return f'ID {self.id} - Nombre: {self.first_name} {self.last_name}'
