# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from .views import IndexView
from .api_views import *

house_router = routers.DefaultRouter()
house_router.register('house', HouseViewSet)
house_router.register('room', RoomViewSet)
house_router.register('requirement', RequirementViewSet)

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='index'),
]

urlpatterns += house_router.urls
