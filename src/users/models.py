# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from locations.models import *
from django.db.models.query import QuerySet

# python3 manage.py makemigrations users
# python3 manage.py migrate

class QuerySetManager(models.Manager):
    def get_query_set(self):
        return self.model.QuerySet(self.model, using=self._db)

    def __getattr__(self, attr, *args):
        return getattr(self.get_query_set(), attr, *args)

USER_TYPE={1:'学生',2:'中介'}
ID_TYPE={1:'护照',2:'驾照',3:'身份证',4:'学生证'}
GENDER={1:'男',2:'女'}
STATUS={1:'普通用户',2:'VIP'}
class Profile(models.Model):
    user=models.OneToOneField(User,verbose_name='账号',related_name="profile")
    nickName=models.CharField(max_length=20, verbose_name='昵称')
    gender=models.SmallIntegerField(default=1,choices=GENDER.items(), verbose_name='性别')
    headIcon=models.ImageField(upload_to='images/profile/',
        default='commons/images/head_portrait.jpg', verbose_name='头像')
    school=models.ForeignKey(Location,blank=True,null=True,verbose_name='学校',related_name="profiles")
    userType=models.SmallIntegerField(default=1,choices=USER_TYPE.items(), verbose_name='用户类型')
    major=models.CharField(max_length=20, verbose_name='专业')
    interests=models.CharField(max_length=255, default='', verbose_name='爱好')
    wechat=models.CharField(blank=True,null=True,max_length=32,verbose_name='微信')
    QQ=models.IntegerField(blank=True,null=True,verbose_name='QQ')
    tel=models.CharField(blank=True,null=True,max_length=30,verbose_name='电话')
    verified=models.BooleanField(verbose_name='实名认证', default=False,
        help_text='是否通过了实名认证')
    credits=models.IntegerField(default=0,verbose_name='信誉')
    nCredits=models.IntegerField(default=0,verbose_name='信誉')
    status=models.SmallIntegerField(default=1,choices=STATUS.items(), verbose_name='头衔')

    class Meta:
        verbose_name_plural = verbose_name = '个人信息'

    def __str__(self):
        return self.nickName+':'+self.user.username

class RealNameVerify(models.Model):
    user=models.OneToOneField(User,verbose_name='账号',related_name="realNameVerify")
    IDType=models.SmallIntegerField(default=1,choices=ID_TYPE.items(), verbose_name='证件类型')
    IDNumber=models.CharField(max_length=50, verbose_name='证件号码')
    IDPhoto=models.ImageField(upload_to='images/realNameVerify/',
        default='commons/images/placeholder.png', verbose_name='证件个人信息页')
    modTime=models.DateTimeField(auto_now=True)

#  class UserProxy(User):

    #  class Meta:
        #  proxy = True
        
    #  objects = QuerySetManager()

    #  class QuerySet(QuerySet):

        #  def get_or_none(self, *args, **kwargs):
            #  """
            #  Performs the query and returns a single object matching the given
            #  keyword arguments.
            #  """
            #  clone = self.filter(*args, **kwargs)
            #  if self.query.can_filter() and not self.query.distinct_fields:
                #  clone = clone.order_by()
            #  num = len(clone)
            #  if num == 1:
                #  return clone._result_cache[0]
            #  if not num:
                #  return None

