from django.urls import path

from .views import *

urlpatterns = [
    path('', login_site, name='login-site'),
    path('logout_site/', logout_site, name='logout-site'),
]
