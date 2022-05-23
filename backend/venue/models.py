from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField('Zip Code', max_length=10)

    def __str__(self):
        return self.name
