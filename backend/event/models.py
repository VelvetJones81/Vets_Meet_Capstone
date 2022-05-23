from django.db import models
from venue.models import Venue

# Create your models here.
class Event(models.Model):
    name = models.CharField('Event Name', max_length=255)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    organizer = models.CharField(max_length=255)
    description = models.TextField(blank= True)

    def __str__(self):
        return self.name