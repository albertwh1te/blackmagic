# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Payment(models.Model):
    user=models.ForeignKey(User,verbose_name='账号',related_name="payments")
    amount=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='数目')
    purpose=models.CharField(max_length=255, verbose_name='目的')
    done=models.BooleanField(verbose_name='已经支付', default=False,
        help_text='是否已经成功支付')
    stage=models.SmallIntegerField(default=1, verbose_name='阶段')
    modTime=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = verbose_name = '支付'
    def __str__(self):
        return self.purpose
