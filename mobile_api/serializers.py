from rest_framework import serializers
from .models import MobileData

class MobileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileData
        fields = '__all__'
