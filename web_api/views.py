from rest_framework import viewsets
from .models import WebData
from .serializers import WebDataSerializer


class WebDataViewSet(viewsets.ModelViewSet):
    queryset = WebData.objects.all()
    serializer_class = WebDataSerializer

