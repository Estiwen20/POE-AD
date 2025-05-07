from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import LoroViewSet

router = DefaultRouter()
router.register(r'', LoroViewSet)

urlpatterns = [
    path('loros/', include(router.urls)),
]
