from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    paginas = models.IntegerField()
    año_publicacion = models.IntegerField()

    def __str__(self):
        return self.titulo