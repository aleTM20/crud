from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from crud.model_resource import PersonResource
from crud.models import Person


class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource


admin.site.register(Person, PersonAdmin)
