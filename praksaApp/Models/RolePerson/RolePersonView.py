from .RolePersonModel import RolePerson
from .RolePersonSerializer import RolePersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def RolePersonGetAll(request):
    rolePerson = RolePerson.objects.all().distinct()
    serializer = RolePersonSerializer(rolePerson, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def RolePersonAdd(request):
    serializer = RolePersonSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def RolePersonGetById(request, id):
    try:
        rolePerson = RolePerson.objects.get(rolePersonId = id)
    except RolePerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = RolePersonSerializer(rolePerson)
    return Response(serializer.data)

@api_view(['PUT'])
def RolePersonPut(request, id):
    try:
        rolePerson = RolePerson.objects.get(rolePersonId = id)
    except RolePerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = RolePersonSerializer(rolePerson, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def RolePersonDelete(request, id):
    try:
        rolePerson = RolePerson.objects.get(rolePersonId = id).delete()
    except RolePerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    
@api_view(['GET'])
def RoleGetByUser(request, id):
    try:
        role = RolePerson.objects.filter(personId_id = id).distinct()
    except RolePerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = RolePersonSerializer(role, many=True)
    return Response(serializer.data)