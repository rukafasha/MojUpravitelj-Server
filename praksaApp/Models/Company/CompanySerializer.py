from rest_framework import serializers
import CompanyModel

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel.Company
        fields = '__all__'