from rest_framework import serializers
from  .AppartmentModel import Appartment

class AppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartment
        fields = '__all__'