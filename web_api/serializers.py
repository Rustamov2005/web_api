from rest_framework import serializers
from .models import WebData


class WebDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebData
        fields = '__all__'
