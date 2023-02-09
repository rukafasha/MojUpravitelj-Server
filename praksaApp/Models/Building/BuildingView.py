from django.forms import model_to_dict
from praksaApp.Models.Appartment.AppartmentModel import Appartment
from praksaApp.Models.Appartment.AppartmentSerializer import AppartmentSerializer
from praksaApp.Models.AppartmentPerson.AppartmentPersonModel import AppartmentPerson
from praksaApp.Models.Person.PersonModel import Person
from .BuildingModel import Building
from .BuildingSerializer import BuildingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def BuildingGetAll(request):
    building = Building.objects.all().distinct()
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
        building = Building.objects.get(buildingId = id).delete()
    except Building.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    
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
        building = Building.objects.filter(companyId = id).order_by("address").distinct()
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


@api_view(['GET'])
def GetBuildingsByAddress(request, address):
    try:
        buildings = Building.objects.filter(address = address)
        
        
    except Building.DoesNotExist:
        return Response("Buildings not found.",status=status.HTTP_404_NOT_FOUND)

    building_details = []

    for building in buildings:
        building_details.append({
            "buildingId":building.buildingId,
            "address":building.address,
            "numberOfApartments":building.numberOfAppartment,
            "countyName":building.countyId.countyName,
            "countryName":building.countyId.countryId.countryName,
            "representativeId":building.representativeId.personId,
            "representativeFirstName":building.representativeId.firstName,
            "representativeLastName":building.representativeId.lastName,
            "companyId":building.companyId.companyId,
            "companyName":building.companyId.companyName,
            })
    
    return Response(building_details)