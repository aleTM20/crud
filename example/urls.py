"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('user.urls')),
                  path('crud/', include('crud.urls')),
                  path('admin/', admin.site.urls),
                  path('administrator/', include('administrator.urls')),
                  path('employee/', include('employee.urls')),
                  path('crudApi/v1/', include('administrator.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)