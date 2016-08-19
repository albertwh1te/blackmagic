# coding:utf-8
from rest_framework import serializers
from menu.models import Menu
from django.contrib.auth.models import User
from explorer.models import Query


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','id')


class MenuSerializer(serializers.ModelSerializer):
    creater = UserSerializer()
    mender = UserSerializer()

    class Meta:
        model = Menu
        depth = 5


class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password',)


class QuerySerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    creater = UserSerializer()
    mender = UserSerializer()

    class Meta:
        model = Query


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
