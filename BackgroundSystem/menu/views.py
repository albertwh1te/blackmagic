# coding:utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from menu.models import Menu,TreeMenu
from menu.serializers import MenuSerializer, UserSerializer, LoginSerializer, PasswordSerializer, QuerySerializer
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import detail_route, list_route
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import status
from explorer.models import Query
from guardian.shortcuts import get_objects_for_user
from django.template import RequestContext


# Create your views here.
#  class MenuListView(ListAPIView):
    #  queryset = Query.objects.all()
    #  serializer_class = QuerySerializer


def display_tree(nodes, leaves):

    display_list = []
    for node in nodes:

        display_list.append(node)
        children = node.children.all()

        node_leaves = leaves.filter(menu=node)

        if len(children) > 0:
            display_list.append(display_tree(children, leaves))
            node_leaves = leaves.filter(menu=node)
        else:
            if node_leaves.exists():
                tmp = []
                for leaf in node_leaves:
                    tmp.append(leaf)
                display_list.append(tmp)

    return display_list


#  class MenuListView(ListView):
    #  template_name = 'menu/menu_list.html'

    #  def get_queryset(self):
        #  user = self.request.user
        #  menus = get_objects_for_user(user, 'explorer.add_query')
        #  return menus

def menu_tree_view(request):
    user = request.user
    menus = get_objects_for_user(user, 'menu.add_menu').filter(parent=None)
    funcs = get_objects_for_user(user, 'explorer.add_query')
    menu_tree = display_tree(menus, funcs)
    return render_to_response('menu/menu_list.html', {'menus': menu_tree})


class QueryListView(ListView):
    template_name = 'menu/query_list.html'
    
    def get_queryset(self):
        user = self.request.user
        queries = get_objects_for_user(user, 'explorer.add_query')
        return queries
       

def tree_menu(request):
        return render_to_response("menu/tree_menu.html",
                                  {'nodes': TreeMenu.objects.all()}
                                  )


class LoginView(GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return Response({'state': True})
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
