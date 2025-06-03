from django.db import models
from .autor import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo
