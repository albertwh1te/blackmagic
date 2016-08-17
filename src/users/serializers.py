from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import User

error_messages={
    'blank':'此处不能为空！',
    'max_length':'您的输入太长',
    'min_length':'您的输入太短！',
    'unique':'该email已经注册！'
}

class UserSerializer(serializers.ModelSerializer):
    #profile = serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password')
        
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_null=True,source='user.username',error_messages=error_messages)
    email=serializers.EmailField(source='user.email',error_messages=error_messages)
    password=serializers.CharField(source='user.password',error_messages=error_messages)
    first_name=serializers.CharField(required=False, allow_null=True,source='user.first_name',error_messages=error_messages)
    last_name=serializers.CharField(required=False, allow_null=True,source='user.last_name',error_messages=error_messages)
    nickName=serializers.CharField(max_length=20,error_messages=error_messages)
    gender=serializers.IntegerField(default=1,error_messages=error_messages)
    headIcon=serializers.ImageField(default='commons/images/head_portrait.jpg',error_messages=error_messages)
    userType=serializers.IntegerField(default=1,error_messages=error_messages)
    major=serializers.CharField(max_length=20,error_messages=error_messages)
    interests=serializers.CharField(max_length=255, default='',error_messages=error_messages)
#    wechat=serializers.CharField(required=False, allow_null=True,max_length=32,error_messages=error_messages)
#    QQ=serializers.IntegerField(required=False, allow_null=True,error_messages=error_messages)
#    tel=serializers.CharField(required=False, allow_null=True,max_length=30,error_messages=error_messages)
    verified=serializers.BooleanField(default=False,error_messages=error_messages)
    credits=serializers.IntegerField(default=0,error_messages=error_messages)
    nCredits=serializers.IntegerField(default=0,error_messages=error_messages)
    status=serializers.IntegerField(default=1,error_messages=error_messages)
    class Meta:
        model = Profile
        fields = ('username', 'first_name','last_name','password','userType', 'nickName', 'gender', 'headIcon','major','interests','email','credits','verified','status','nCredits')

class RealNameVerifySerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = RealNameVerify
        fields=('id','username','IDType','IDPhoto','IDNumber','modTime')

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password',)  

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password')       
    
