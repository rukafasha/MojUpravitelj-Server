from .CountyModel import County
from .CountySerializer import CountySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def CountyList(request):
    if request.method == 'GET':
        county = County.objects.all()
        serializer = CountySerializer(county, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CountySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def CountyDetail(request, id):
    
    try:
        county = County.objects.get(countyId = id)
    except County.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CountySerializer(county)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CountySerializer(county, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        county.isActive = False
        serializer = CountySerializer(county)
        serializer.save()
        