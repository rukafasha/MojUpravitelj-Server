from .AppartmentModel import Appartment
from .AppartmentSerializer import AppartmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def AppartmentList(request):
    if request.method == 'GET':
        appartment = Appartment.objects.all()
        serializer = AppartmentSerializer(appartment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = AppartmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def AppartmentDetail(request, id):
    
    try:
        appartment = Appartment.objects.get(appartmentId = id)
    except Appartment.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AppartmentSerializer(appartment)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = AppartmentSerializer(appartment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        appartment.isActive = False
        serializer = AppartmentSerializer(appartment)
        serializer.save()
        