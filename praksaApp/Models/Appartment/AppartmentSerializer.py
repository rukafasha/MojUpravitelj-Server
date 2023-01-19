from rest_framework import serializers
import AppartmentModel

class AppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppartmentModel.Appartment
        fields = '__all__'