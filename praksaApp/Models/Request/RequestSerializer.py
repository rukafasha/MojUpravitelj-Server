from rest_framework import serializers

from praksaApp.Models.Request.RequestModel import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'