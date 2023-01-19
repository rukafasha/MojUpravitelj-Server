from .CountryModel import Country
from .CountrySerializer import CountrySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def CountryList(request):
    if request.method == 'GET':
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CountrySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def CountryDetail(request, id):
    
    try:
        country = Country.objects.get(countryId = id)
    except Country.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CountrySerializer(country, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        country.isActive = False
        serializer = CountrySerializer(country)
        serializer.save()
        