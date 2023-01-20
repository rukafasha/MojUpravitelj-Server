from .RolePersonModel import RolePerson
from .RolePersonSerializer import RolePersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def RolePersonList(request):
    if request.method == 'GET':
        rolePerson = RolePerson.objects.all()
        serializer = RolePersonSerializer(rolePerson, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = RolePersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def RolePersonDetail(request, id):
    
    try:
        rolePerson = RolePerson.objects.get(rolePersonId = id)
    except RolePerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RolePersonSerializer(rolePerson)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = RolePersonSerializer(rolePerson, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        rolePerson.isActive = False
        serializer = RolePersonSerializer(rolePerson)
        serializer.save()