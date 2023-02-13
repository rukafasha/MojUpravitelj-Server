from .CountyModel import County
from .CountySerializer import CountySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def CountyGetAll(request):
    county = County.objects.all().distinct()
    serializer = CountySerializer(county, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def CountyAdd(request):
    serializer = CountySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def CountyGetByID(request, id):
    try:
        county = County.objects.get(countyId = id)
    except County.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = CountySerializer(county)
    return Response(serializer.data)
    
@api_view(['PUT'])
def CountyPut(request, id):
    try:
        county = County.objects.get(countyId = id)
    except County.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = CountySerializer(county, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def CountyDelete(request, id):
    try:
        county = County.objects.get(countyId = id).delete()
    except County.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def getCountyByCountry(request, string):
    try:
        county = County.objects.filter(countryId__countryName = string)
    except County.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = CountySerializer(county, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCountyByName(request, string):
    try:
        county = County.objects.get(countyName = string)
    except County.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = CountySerializer(county)
    return Response(serializer.data)
