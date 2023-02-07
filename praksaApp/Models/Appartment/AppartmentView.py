from .AppartmentModel import Appartment
from .AppartmentSerializer import AppartmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def AppartmentGetAll(request):
    appartment = Appartment.objects.all().distinct()
    serializer = AppartmentSerializer(appartment, many=True)
    print("helloo get")
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AppartmentAdd(request):
    serializer = AppartmentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print("helloo post")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def AppartmentGetById(request, id):
    try:
        appartment = Appartment.objects.get(appartmentId = id)
    except Appartment.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = AppartmentSerializer(appartment)
    return Response(serializer.data)

@api_view(['PUT'])
def AppartmentPut(request, id):
    try:
        appartment = Appartment.objects.get(appartmentId = id)
    except Appartment.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = AppartmentSerializer(appartment, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def AppartmentDelete(request, id):
    try:
        appartment = Appartment.objects.get(appartmentId = id).delete()
    except Appartment.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

        