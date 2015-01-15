from django.contrib import admin

from vallejo_watch.visualize.models import Incident


class IncidentAdmin(admin.ModelAdmin):

    list_display = ('timestamp', 'address', 'status', 'y_pos', 'x_pos')
    readonly_fields = ('x_pos', 'y_pos',)

admin.site.register(Incident, IncidentAdmin)
