# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

HOUSE_TYPE = {1: '公寓', 2: '别墅', 3: '工作室'}
FURNISH_TYPE = {1: '齐全', 2: '部分', 3: '无'}
PET_POLICY = {1: '允许', 2: '可商量', 3: '不允许'}
LEASE_TERM = {1: '长租', 2: '短租', 3: '可商量'}


class House(models.Model):
    address = models.CharField(max_length=255, verbose_name='地址', unique=True)
    dateStart = models.DateTimeField(verbose_name='起租日期')
    houseType = models.SmallIntegerField(choices=HOUSE_TYPE.items(), verbose_name='类型')
    structure = models.CharField(max_length=100, verbose_name='户型')
    furnishType = models.SmallIntegerField(choices=FURNISH_TYPE.items(), verbose_name='家具')
    rent = models.IntegerField(default=1, verbose_name='月租')
    deposit = models.IntegerField(default=0, verbose_name='押金')
    petPolicy = models.SmallIntegerField(choices=PET_POLICY.items(), verbose_name='宠物')
    utilities = models.CharField(default="wifi|water|electricity|in-laundry", max_length=255, verbose_name='设施')
    status = models.BooleanField(verbose_name='是否可入住', default=False,
                                 help_text='是否可入住')
    leaseTerm = models.SmallIntegerField(default=1, choices=LEASE_TERM.items(), verbose_name='租期')
    photo = models.ImageField(upload_to='image/house/',
                              default='image/default/house.jpg', verbose_name='照片')
    modTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = '房源'

    def __str__(self):
        return "%s" % self.address


ROOM_TYPE = {1: '主卧', 2: '侧卧', 3: '客厅'}
BATH_TYPE = {1: '独立', 2: '共用', 3: '无'}
CAPACITY = {1: '1', 2: '2', 3: '3'}
GENDER = {1: '男生', 2: '女生', 3: '男女均可'}


class Room(models.Model):
    roomType = models.SmallIntegerField(choices=ROOM_TYPE.items(), verbose_name='类型')
    house = models.ForeignKey(House, verbose_name='从属的房屋', related_name="rooms")
    rent = models.IntegerField(default=1, verbose_name='月租/人')
    deposit = models.IntegerField(default=0, verbose_name='押金')
    bathType = models.SmallIntegerField(choices=BATH_TYPE.items(), verbose_name='卫生间')
    dateStart = models.DateTimeField(verbose_name='起租日期')
    capacity = models.SmallIntegerField(default=1, choices=CAPACITY.items(), verbose_name='总共床位数')
    vacancy = models.SmallIntegerField(default=1, choices=CAPACITY.items(), verbose_name='剩余床位数')
    leaseTerm = models.SmallIntegerField(default=1, choices=LEASE_TERM.items(), verbose_name='租期')
    status = models.BooleanField(verbose_name='是否可入住', default=False,
                                 help_text='是否可入住')
    furnishType = models.SmallIntegerField(choices=FURNISH_TYPE.items(), verbose_name='家具')
    photo = models.ImageField(upload_to='image/room/',
                              default='image/default/room.jpg', verbose_name='照片')
    roommates = models.ForeignKey(User, verbose_name='室友', related_name="roomsLived")
    applicants = models.ForeignKey(User, verbose_name='申请者', related_name="applications")
    gender = models.SmallIntegerField(default=3, choices=GENDER.items(), verbose_name='室友性别要求')
    modTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = '房间'

    def __str__(self):
        return str(self.roomType)


class Requirement(models.Model):
    roomType = models.SmallIntegerField(choices=ROOM_TYPE.items(), verbose_name='类型')
    maxRent = models.IntegerField(default=1, verbose_name='月租/人')
    bathType = models.SmallIntegerField(choices=BATH_TYPE.items(), verbose_name='卫生间')
    dateStart = models.DateTimeField(verbose_name='起租日期')
    vacancy = models.SmallIntegerField(default=1, choices=CAPACITY.items(), verbose_name='剩余床位数')
    leaseTerm = models.SmallIntegerField(default=1, choices=LEASE_TERM.items(), verbose_name='租期')
    furnishType = models.SmallIntegerField(choices=FURNISH_TYPE.items(), verbose_name='家具')
    distanceToSchool = models.IntegerField(default=10, verbose_name='到学校步行时间')
    distanceToSuperMarket = models.IntegerField(default=10, verbose_name='到超市步行时间')
    petPolicy = models.SmallIntegerField(choices=PET_POLICY.items(), verbose_name='宠物')
    utilities = models.CharField(default="wifi|water|electricity|in-laundry", max_length=255, verbose_name='设施')

    class Meta:
        verbose_name_plural = verbose_name = '需求'

    def __str__(self):
        return str(self.roomType)


class Collection(models.Model):
    '''
    用户收藏某个产品
    '''
    create_time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,verbose_name="收藏者")

    house = models.ForeignKey(House,verbose_name="收藏的房屋")
    
    class Meta:
        verbose_name = verbose_name_plural = '收藏记录'

    def __str__(self):
        return  str(self.user) + ':' + str(self.product)



