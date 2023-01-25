from rest_framework import serializers
from .CountyModel import County

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'