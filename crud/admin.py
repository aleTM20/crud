from django.contrib import admin

# Register your models here.
from crud.models import Person

admin.site.register(Person)
