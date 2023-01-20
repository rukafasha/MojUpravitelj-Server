from .AppartmentPersonModel import AppartmentPerson
from .AppartmentPersonSerializer import AppartmentPersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def AppartmentPersonList(request):
    if request.method == 'GET':
        appartmentPerson = AppartmentPerson.objects.all()
        serializer = AppartmentPersonSerializer(appartmentPerson, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = AppartmentPersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def AppartmentPersonDetail(request, id):
    
    try:
        appartmentPerson = AppartmentPerson.objects.get(appartmentPersonId = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AppartmentPersonSerializer(appartmentPerson)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = AppartmentPersonSerializer(appartmentPerson, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        appartmentPerson.isActive = False
        serializer = AppartmentPersonSerializer(appartmentPerson)
        serializer.save()
        