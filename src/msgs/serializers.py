from rest_framework import serializers
from msgs.models import *


class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = ('id', 'title', 'content', 'sender', 'receiver', 'time')