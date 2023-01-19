from rest_framework import serializers
import ReportModel

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportModel.Report
        fields = '__all__'