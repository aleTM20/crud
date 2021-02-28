from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='admistrator'),
    path('personList/', person_list, name='admistrator-person-list'),
    path('createPerson/', create_person, name='admistrator-create-person'),
]
