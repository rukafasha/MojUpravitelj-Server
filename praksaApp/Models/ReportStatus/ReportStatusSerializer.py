from rest_framework import serializers
from .ReportStatusModel import ReportStatus

class ReportStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportStatus
        fields = '__all__'