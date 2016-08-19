"""BackgroundSystem URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

def html_view(*args, **kwargs):
    return TemplateView.as_view(template_name=kwargs['template_name'])(*args, **kwargs)

urlpatterns = [
    url('^$',TemplateView.as_view(template_name='commons/index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^explorer/', include('explorer.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api_menus/', include('menu.urls')),
    url(r'^(?P<template_name>.+.html)$',html_view),
]
