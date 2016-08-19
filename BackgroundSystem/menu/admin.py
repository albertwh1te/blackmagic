# coding:utf-8
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from menu.models import Menu, TreeMenu

from mptt.admin import MPTTModelAdmin
# Register your models here.


admin.site.register(TreeMenu, MPTTModelAdmin)

class MenusAdmin(GuardedModelAdmin):
    pass

admin.site.register(Menu, MenusAdmin)
#  admin.site.register(models.Menus)

