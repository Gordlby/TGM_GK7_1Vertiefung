from sys import maxsize

from django.db import models

# Create your models here.
class Fach(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    zu_niedrig = models.IntegerField(default=0)
    genau_richtig = models.IntegerField(default=0)
    zu_hoch = models.IntegerField(default=0)
    def __str__(self):
        return self.name
