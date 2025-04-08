from django.db import models

class Loro(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    alas = models.IntegerField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
