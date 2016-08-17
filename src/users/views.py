# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
# from django.http import JsonResponse
# from django.contrib.auth.models import User
# from offcampus.settings import EMAIL_HOST_USER
# from django.template import loader
# from django.core.mail import EmailMultiAlternatives
# from .models import Profile, UserProxy
# from django.views import generic

#caozhenfeng's---
from rest_framework import viewsets,renderers,permissions
from rest_framework.decorators import detail_route, list_route
from users.models import *
from commons.permissions import *
from users.serializers import *
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib import auth
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import logging
from rest_framework import authentication
from rest_framework import exceptions
# Get an instance of a logger
logger = logging.getLogger('mylogger')
#-----

# class LoginView(generic.View):
#     def post(self, request, *args, **kwargs):
#         email = request.POST.get('email', False)
#         password = request.POST.get('password', False)

#         user = User.objects.get(email=email)
#         if user.check_password(password):
#             return JsonResponse({'fail': False})
#         return JsonResponse({'fail': True})


# class SignupView(generic.TemplateView):
#     template_name = 'users/signup.html'
#     model = Profile

#     def send_email(self, context, from_email, to_email, html_email_template_name=None):
#         subject = "中国留学生租房"
#         email_message = EmailMultiAlternatives(subject, '', from_email, [to_email])

#         if html_email_template_name:
#             html_email = loader.render_to_string(html_email_template_name, context)
#             email_message.attach_alternative(html_email, 'text/html')
#         email_message.send()

#     def post(self, request, *args, **kwargs):
#         email = request.POST.get('email', False)
#         gender = request.POST.get('gender', False)
#         userType = request.POST.get('userType', False)
#         nickname = request.POST.get('nickname', False)
#         major = request.POST.get('major', False)
#         introduction = request.POST.get('introduction', False)
#         password = request.POST.get('password', False)
#         password_verify = request.POST.get('password_verify', False)

#         if not email or not nickname or not major or not introduction or not password or not password_verify:
#             return JsonResponse({'fail': True, 'type': 'complete'})

#         if password != password_verify:
#             return JsonResponse({'fail': True, 'type': 'match'})

#         user = UserProxy.objects.get_or_none(email=email)
#         if user:
#             return JsonResponse({'fail': True, 'type': 'exist'})

#         user = User.objects.create_user(username=nickname, password=password, email=email)
#         user.save()
#         profile = Profile(user=user, gender=gender, userType=userType, major=major, introduction=introduction)
#         profile.save()

#         context = {
#             'email': email,
#             'username': nickname,
#         }
#         # 發送郵件
#         self.send_email(context, EMAIL_HOST_USER, email, html_email_template_name='users/email/email_confirm_template.html')
#         return JsonResponse({'fail': False})


# class SignupSuccessView(generic.TemplateView):
#     '''
#     註冊成功
#     '''
#     template_name = 'users/signup-success.html'



# @login_required

# Create your views here.
#caozhenfeng's ----
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsSelfOrReadOnly)

    @detail_route(methods=['post'],permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsSelfOrReadOnly])
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
            email=serializer.validated_data['email']
            users=User.objects.filter(email=email)
            if len(users)>0:
                username=users[0].username
                password=serializer.validated_data['password']
                user = auth.authenticate(username=username, password=password)
                if user:
                    auth.login(request,user)
                    return Response({'state':True})

        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)    
    @list_route(methods=['get'],permission_classes=[permissions.AllowAny])
    def logout(self,request):
        logout(request)
        return redirect('/')

class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def update(self, serializer):
        data=self.request.data
        user_serializer = UserSerializer(self.request.user,data=data)
        profile=Profile.objects.filter(user=self.request.user)[0]
        profile_serializer=ProfileSerializer(profile,data=data)
        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()

    @list_route(methods=['post','option'],permission_classes=[permissions.AllowAny])
    def signup(self, request):
        data=request.data
        user=User.objects.filter(email=data.get('email',None))
        err={}
        user_serializer = UserSerializer(data=data)
        profile_serializer=ProfileSerializer(data=data)
        valid=user_serializer.is_valid() 
        valid=(profile_serializer.is_valid() and valid)
        err.update(user_serializer.errors)
        err.update(profile_serializer.errors)
        if (len(user)==0 and valid):
            user=user_serializer.save(username=user_serializer.validated_data['email'][0:30])
            user.set_password(user_serializer.validated_data['password'])
            user.save()
            profile=profile_serializer.save(user=user)
            return Response({'success':True})
        if (len(user)>0):
            err.update({'email':'该email已经注册过了！'})
        return Response(err)

    @list_route(methods=['get'],permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsSelfOrReadOnly])
    def get_current(self, request, *args, **kwargs):
        current = get_object_or_404(self.queryset, user=request.user.pk)
        current=ProfileSerializer(current)
        return Response(current.data)



#-----
