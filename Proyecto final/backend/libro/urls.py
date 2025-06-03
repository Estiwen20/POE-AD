from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet

routers = DefaultRouter()
routers.register(prefix='', viewset=LibroViewSet)

urlpatterns = [
 path('', include(routers.urls)),
]