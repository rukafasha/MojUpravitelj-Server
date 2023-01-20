from .AppartmentPersonModel import AppartmentPerson
from .AppartmentPersonSerializer import AppartmentPersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def AppartmentPersonGetAll(request):
    appartmentPerson = AppartmentPerson.objects.all()
    serializer = AppartmentPersonSerializer(appartmentPerson, many=True)        
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def AppartmentPersonAdd(request):
    serializer = AppartmentPersonSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def AppartmentPersonGetById(request, id):
    try:
        appartmentPerson = AppartmentPerson.objects.get(appartmentPersonId = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = AppartmentPersonSerializer(appartmentPerson)        
    return Response(serializer.data)

@api_view(['PUT'])
def AppartmentPersonPut(request, id):
    try:
        appartmentPerson = AppartmentPerson.objects.get(appartmentPersonId = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = AppartmentPersonSerializer(appartmentPerson, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def AppartmentPersonDelete(request, id):
    try:
        appartmentPerson = AppartmentPerson.objects.get(appartmentPersonId = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    appartmentPerson.isActive = False
    serializer = AppartmentPersonSerializer(appartmentPerson)
    serializer.save()
        