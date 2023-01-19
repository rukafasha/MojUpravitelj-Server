from rest_framework import serializers
import BuildingModel

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingModel.Building
        fields = '__all__'