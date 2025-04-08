from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LoroViewSet

router = DefaultRouter()
router.register(r'loros', LoroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
