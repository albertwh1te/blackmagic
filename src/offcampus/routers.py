from rest_framework.routers import DefaultRouter
from users.views import *
from searches.views import *
from django.conf.urls import url,include

router = DefaultRouter()
router.register(r'users/profiles',ProfileViewSet)
router.register(r'users/users',UserViewSet)
router.register(r'searches',HouseListView)




