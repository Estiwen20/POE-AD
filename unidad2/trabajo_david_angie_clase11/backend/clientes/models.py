
from django.db import models

class Loro(models.Model):
    nombre = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=100)
    edad = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre