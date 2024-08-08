from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MobileDataViewSet

router = DefaultRouter()
router.register(r'data', MobileDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
