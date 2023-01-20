from rest_framework import serializers
from .AppartmentPersonModel import AppartmentPerson

class AppartmentPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppartmentPerson
        fields = '__all__'