from rest_framework import viewsets
from .models import MobileData
from .serializers import MobileDataSerializer

class MobileDataViewSet(viewsets.ModelViewSet):
    queryset = MobileData.objects.all()
    serializer_class = MobileDataSerializer
