from rest_framework import serializers
import CountryModel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel.Country
        fields = '__all__'