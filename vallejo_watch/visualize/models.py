from django.db import models

from vallejo_watch.utils.geo import geocode

class Incident(models.Model):
    OPEN = 'op'
    CLOSED = 'cl'

    NOISE_COMPLAINT = 'nc'
    GRAFFITI = 'gr'

    STATUS_CHOICES = ((OPEN, 'Open'),
                      (CLOSED, 'Closed'))

    ISSUE_CHOICES = ((NOISE_COMPLAINT, 'Noise Complaint'),
                     (GRAFFITI, 'Graffiti'))

    timestamp = models.DateTimeField()
    address = models.CharField(max_length=256)
    x_pos = models.FloatField(null=True, blank=True)  # TODO: change lat and lon to a single geom type for PostGIS
    y_pos = models.FloatField(null=True, blank=True)
    status = models.CharField(null=True, blank=True, max_length=2, choices=STATUS_CHOICES)
    issue_type = models.CharField(null=True, blank=True, max_length=2, choices=ISSUE_CHOICES)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        print self.x_pos, self.y_pos
        if self.address != None:
            point = geocode(self.address)
            self.y_pos = point.lat
            self.x_pos = point.lon

        super(Incident, self).save(*args, **kwargs)
