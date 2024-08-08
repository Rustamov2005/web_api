from rest_framework import serializers
from .models import BotMessage

class BotMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotMessage
        fields = '__all__'
