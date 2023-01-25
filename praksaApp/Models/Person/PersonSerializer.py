from rest_framework import serializers
from .PersonModel import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'