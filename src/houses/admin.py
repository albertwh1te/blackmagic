from django.contrib import admin

# Register your models here.

from .models import *

admin.site.site_header = 'OFFCAMPUS'
admin.site.site_title = 'OFFCAMPUS'
admin.site.register(House)
admin.site.register(Room)
admin.site.register(Requirement)
