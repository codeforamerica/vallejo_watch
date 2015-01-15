import json

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from vallejo_watch.visualize.models import Incident


def home(request):
    incidents = Incident.objects.all().values_list('x_pos', 'y_pos')
    incidents_json = json.dumps(list(incidents), cls=DjangoJSONEncoder)

    # TODO: add fields to the incident objects so that we can support filtering

    return render(request, 'index.html', {'incidents': incidents_json})
