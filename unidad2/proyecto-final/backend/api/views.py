from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'nombre', 'nacionalidad', 'edad']
    search_fields = ['nombre', 'nacionalidad']

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'titulo', 'genero', 'paginas', 'anio']
    search_fields = ['titulo', 'genero']
