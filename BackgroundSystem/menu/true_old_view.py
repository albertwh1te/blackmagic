# coding:utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from menu.models import Menu
from menu.serializers import MenuSerializer,UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework import viewsets,renderers,permissions
from rest_framework.decorators import detail_route, list_route
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import exceptions


# Create your views here.
class MenuListView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UserViewSet(viewsets.ViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = User.objects.all()
    #  serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    @detail_route(methods=['post'],permission_classes=[permissions.IsAuthenticated])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)
    

    #@csrf_exempt
    #@ensure_csrf_cookie
    @list_route(methods=['post','option'],permission_classes=[permissions.AllowAny])
    def login(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username =serializer.validated_data['username']
            #  users=User.objects.filter(email=email)
#              if len(users)>0:
                #  username=users[0].username
            password=serializer.validated_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request,user)
                return Response({'state':True})

        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['get'],permission_classes=[permissions.IsAuthenticated])
    def logout(self,request):
        auth.logout(request)
        return redirect('/')
   
    
