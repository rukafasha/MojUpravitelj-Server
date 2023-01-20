from rest_framework import serializers
from .RolePersonModel import RolePerson

class RolePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePerson
        fields = '__all__'