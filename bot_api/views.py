from rest_framework import viewsets
from .models import BotMessage
from .serializers import BotMessageSerializer

class BotMessageViewSet(viewsets.ModelViewSet):
    queryset = BotMessage.objects.all()
    serializer_class = BotMessageSerializer
