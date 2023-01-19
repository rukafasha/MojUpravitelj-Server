from rest_framework import serializers
import ReportStatusModel

class ReportStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportStatusModel.ReportStatus
        fields = '__all__'