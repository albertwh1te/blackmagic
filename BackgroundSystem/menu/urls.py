# coding:utf-8
from django.conf.urls import url, include
from menu import views

urlpatterns = [
    url(r'^tree_menu$',views.tree_menu,name='treelist'),
    url(r'^menu$',views.menu_tree_view,name='menu_list'),
    url(r'^queries$',views.QueryListView.as_view(),name='querylist'),
    url(r'^login_api$', views.LoginView.as_view(), name='login'),
]

