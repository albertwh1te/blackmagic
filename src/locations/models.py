# -*- coding: utf-8 -*-
from django.db import models

from houses.models import House

# Create your models here.
LOCATION_TYPE = {1: '学校', 2: '地铁站', 3: '超市'}


class Location(models.Model):
    name = models.CharField(max_length=200, verbose_name='名称', unique=True)
    address = models.CharField(max_length=255, verbose_name='地址', unique=True)
    locationType = models.SmallIntegerField(choices=LOCATION_TYPE.items(), verbose_name='类型')
    icon = models.ImageField(upload_to='image/location/icon/',
                             default='image/default/location.jpg', verbose_name='照片')
    description = models.TextField(max_length=1000, verbose_name='描述')

    class Meta:
        verbose_name_plural = verbose_name = '位标地址'

    def __str__(self):
        return "%s" % self.name


class Distance(models.Model):
    house = models.ForeignKey(to=House, verbose_name=u'房屋位置')
    nearLocation = models.ForeignKey(to=Location, verbose_name=u'附近位标')
    walk = models.IntegerField(default=0, verbose_name='步行(分钟)', help_text=u'到附近位标步行时间', blank=True)
    station = models.IntegerField(default=0, verbose_name='地铁站数目', blank=True)
    drive = models.IntegerField(default=0, verbose_name='自驾 (分钟)', blank=True)
    walkingTime = models.IntegerField(default=0, verbose_name='共计步行时间 (分钟)', blank=True)

    def save(self, *args, **kwargs):
        self.walkingTime = max(self.walk + self.station * 5 + 10, self.drive * 8)
        super(Distance, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = verbose_name = '周边信息'

    def __str__(self):
        return str(self.walkingTime) + " 分钟"
