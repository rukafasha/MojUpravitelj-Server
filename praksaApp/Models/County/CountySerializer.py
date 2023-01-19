from rest_framework import serializers
import CountyModel

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountyModel.County
        fields = '__all__'