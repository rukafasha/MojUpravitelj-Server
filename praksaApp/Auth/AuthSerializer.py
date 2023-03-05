from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    deviceID = serializers.CharField()

class CompanyRegistrationSerializer(serializers.Serializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    dateOfBirth = serializers.DateField()
    companyName = serializers.CharField()


class RegistrationSerializer(serializers.Serializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    dateOfBirth = serializers.DateField()