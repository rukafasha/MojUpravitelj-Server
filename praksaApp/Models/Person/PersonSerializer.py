from rest_framework import serializers
import PersonModel

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel.Person
        fields = '__all__'