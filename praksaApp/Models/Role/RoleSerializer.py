from rest_framework import serializers
import RoleModel

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel.Role
        fields = '__all__'