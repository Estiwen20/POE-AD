from rest_framework import viewsets
from .models import Loro
from .serializers import LoroSerializer

class LoroViewSet(viewsets.ModelViewSet):
    queryset = Loro.objects.all()
    serializer_class = LoroSerializer
