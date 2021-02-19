from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='employee-index'),
    path('showHello/', show_hello, name='employee-show-hello'),
]
