from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet

routers = DefaultRouter()
routers.register(prefix='', viewset=AutorViewSet)

urlpatterns = [
 path('', include(routers.urls)),
]