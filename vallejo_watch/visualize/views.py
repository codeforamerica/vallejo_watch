import json

from django.shortcuts import render

from vallejo_watch.visualize.models import Incident


def home(request):
    incidents = Incident.objects.all().values_list('x_pos', 'y_pos', 'issue_type', 'address', 'timestamp')
    formatted_incidents = []
    for i in incidents:
        ts_formatted = i[4].strftime("%I:%M %p %b %d, %Y")
        formatted_incidents.append(list(i[:4]) + [ts_formatted])

    incidents_json = json.dumps(formatted_incidents)

    return render(request, 'index.html', {'incidents': incidents_json})
