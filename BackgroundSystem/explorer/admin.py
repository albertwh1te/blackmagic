from django.contrib import admin
from explorer.models import Query
from explorer.actions import generate_report_action
from guardian.admin import GuardedModelAdmin


class QueryAdmin(GuardedModelAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    #  raw_id_fields = ('created_by_user',)
    
    actions = [generate_report_action()]

admin.site.register(Query, QueryAdmin)
