from rest_framework import serializers
from .models import DungeonType

class DungeonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DungeonType
        fields = ['id', 'name', 'description']