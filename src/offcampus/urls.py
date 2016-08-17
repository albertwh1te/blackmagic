"""offcampus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

from commons.conf_page_error import *
from commons.static_utils import static
from offcampus.routers import *
from searches.views import CollectionsCreateListView


def html_view(*args, **kwargs):
    return TemplateView.as_view(template_name=kwargs['template_name'])(*args, **kwargs)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/collections', CollectionsCreateListView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^user/', include('users.urls', namespace="user")),
    url(r'^house/', include('houses.urls', namespace="house")),
    url(r'^msgs/', include('msgs.urls', namespace="msgs")),
    url(r'^$', TemplateView.as_view(template_name="commons/index.html")),
    url(r'^(?P<template_name>.+.html)$',html_view),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
