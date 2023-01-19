from rest_framework import serializers
import UserAccountModel

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountModel.UserAccount
        fields = '__all__'