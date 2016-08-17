# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Msg(models.Model):
    sender = models.ForeignKey(User, verbose_name='发送者', related_name="sentMsgs")
    receiver = models.ForeignKey(User, verbose_name='接收者', related_name="receivedMsgs")
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(max_length=1000, verbose_name='正文')
    formerMsg = models.ForeignKey('Msg', blank=True, null=True, verbose_name='上一条消息', related_name="nextMsg")
    time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(verbose_name='状态：0为未读，1为已读', default=0)

    class Meta:
        verbose_name_plural = verbose_name = '消息'

    def __str__(self):
        return self.title


class Test(models.Model):
    test = models.CharField(max_length=32)

