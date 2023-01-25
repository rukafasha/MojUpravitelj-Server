from rest_framework import serializers
from .BuildingModel import Building

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'