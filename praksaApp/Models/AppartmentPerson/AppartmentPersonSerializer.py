from rest_framework import serializers
import AppartmentPersonModel

class AppartmentPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppartmentPersonModel.AppartmentPerson
        fields = '__all__'