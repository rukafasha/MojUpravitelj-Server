from .BuildingModel import Building
from .BuildingSerializer import BuildingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def BuildingList(request):
    if request.method == 'GET':
        building = Building.objects.all()
        serializer = BuildingSerializer(building, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = BuildingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def BuildingDetail(request, id):
    
    try:
        building = Building.objects.get(countryId = id)
    except Building.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BuildingSerializer(building)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = BuildingSerializer(building, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        building.isActive = False
        serializer = BuildingSerializer(building)
        serializer.save()
        