# -*- coding: utf-8 -*-
from django.db import models
from houses.models import *
# Create your models here.
class Requirement(models.Model):
    roomType=models.SmallIntegerField(choices=ROOM_TYPE.items(), verbose_name='类型')
    maxRent=models.IntegerField(default=1, verbose_name='月租/人')
    bathType=models.SmallIntegerField(choices=BATH_TYPE.items(), verbose_name='卫生间')
    dateStart=models.DateTimeField(verbose_name='起租日期')
    vacancy=models.SmallIntegerField(default=1,choices=CAPACITY.items(), verbose_name='剩余床位数')
    leaseTerm=models.SmallIntegerField(default=1,choices=LEASE_TERM.items(), verbose_name='租期')
    furnishType=models.SmallIntegerField(choices=FURNISH_TYPE.items(), verbose_name='家具')
    distanceToSchool=models.IntegerField(default=10, verbose_name='到学校步行时间')
    distanceToSuperMarket=models.IntegerField(default=10, verbose_name='到超市步行时间')
    petPolicy=models.SmallIntegerField(choices=PET_POLICY.items(), verbose_name='宠物')
    utilities=models.CharField(default="wifi|water|electricity|in-laundry",max_length=255, verbose_name='设施')
    class Meta:
        verbose_name_plural = verbose_name = '需求'
    def __str__(self):
        return str(self.dateStart)
    
