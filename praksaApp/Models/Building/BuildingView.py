from .BuildingModel import Building
from .BuildingSerializer import BuildingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def BuildingGetAll(request):
    building = Building.objects.all()
    serializer = BuildingSerializer(building, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def BuildingAdd(request):
    serializer = BuildingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def BuildingGetByID(request, id):
    try:
        building = Building.objects.get(buildingId = id)
    except Building.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BuildingSerializer(building)
        return Response(serializer.data)
    
@api_view(['PUT'])
def BuildingPut(request, id):
    try:
        building = Building.objects.get(buildingId = id)
    except Building.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = BuildingSerializer(building, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def BuildingDelete(request, id):
    try:
        building = Building.objects.get(buildingId = id)
    except Building.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    building.isActive = False
    serializer = BuildingSerializer(building)
    serializer.save()
    
@api_view(['GET'])
def GetBuildingByUser(request, id):
    try:
        building = Building.objects.get(buildingId__appartmenId__personId = id)
    except Building.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BuildingSerializer(building)
    return Response(serializer.data)

@api_view(['GET'])
def GetBuildingByCompany(request, id):
    try:
        building = Building.objects.filter(companyId = id).order_by("address")
    except Building.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BuildingSerializer(building, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetBuildingByAdress(request, string):
    try:
        building = Building.objects.get(address = string)
    except Building.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BuildingSerializer(building)
    return Response(serializer.data)