from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotMessageViewSet

router = DefaultRouter()
router.register(r'messages', BotMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
