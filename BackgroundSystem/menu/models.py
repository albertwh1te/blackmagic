# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    title = models.CharField(max_length=100)
    decs = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.DateTimeField(auto_now=True)
    modifiedtime = models.DateTimeField(auto_now_add=True)
#      creater = models.ForeignKey(
        #  User, null=True, blank=True, related_name='creater')
    #  mender = models.ForeignKey(
        #  User, null=True, blank=True, related_name='mender')
    #  parent = models.ForeignKey(
        #  'self', null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'sys_menu'
        ordering = ['title']
        verbose_name = verbose_name_plural = 'Menus'

class TreeMenu(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    decs = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.DateTimeField(auto_now=True)
    modifiedtime = models.DateTimeField(auto_now_add=True)
    creater = models.ForeignKey(
        User, null=True, blank=True, related_name='creater')
    mender = models.ForeignKey(
        User, null=True, blank=True, related_name='mender')
   
    def __str__(self):
        return str(self.id)

    
    class MPTTMeta:
        order_insertion_by = ['title']


    

