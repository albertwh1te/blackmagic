from django.contrib import admin

# Register your models here.

from .models import *


class DistanceAdmin(admin.ModelAdmin):
    list_display = ('house', 'nearLocation', 'walk', 'station', 'drive', 'walkingTime')


admin.site.register(Location)
admin.site.register(Distance, DistanceAdmin)
