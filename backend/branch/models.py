from django.db import models

# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length= 25)

