# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from msgs import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register(r'gets', views.GetMsg)
urlpatterns = [
    url(r'^send', views.send),
    url(r'^change', views.change),
    url(r'^delete', views.delete),
    url(r'^', include(router.urls)),
    ]