from rest_framework import serializers
import RolePersonModel

class RolePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePersonModel.RolePerson
        fields = '__all__'