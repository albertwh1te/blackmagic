from rest_framework import serializers

from .models import *


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement