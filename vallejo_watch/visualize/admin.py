from django.contrib import admin

from vallejo_watch.visualize.models import Incident


class IncidentAdmin(admin.ModelAdmin):

    list_display = ('timestamp', 'address', 'y_pos', 'x_pos', 'issue_type')
    readonly_fields = ('x_pos', 'y_pos',)

admin.site.register(Incident, IncidentAdmin)
