from sys import maxsize

from django.db import models

# Create your models here.
class Fach(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Antwort(models.Model):
    choice = models.IntegerField(default=0)
    fach = models.ForeignKey(Fach, on_delete=models.CASCADE)
    def __str__(self):
        return self.fach.name