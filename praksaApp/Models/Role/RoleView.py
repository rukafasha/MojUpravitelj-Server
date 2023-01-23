from .RoleModel import Role
from .RoleSerializer import RoleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def RoleGetAll(request):
    role = Role.objects.all()
    serializer = RoleSerializer(role, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def RoleAdd(request):
    serializer = RoleSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def RoleGetById(request, id):
    try:
        role = Role.objects.get(roleId = id)
    except Role.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = RoleSerializer(role)
    return Response(serializer.data)

@api_view(['PUT'])
def RolePut(request, id):
    try:
        role = Role.objects.get(roleId = id)
    except Role.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = RoleSerializer(role, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def RoleDelete(request, id):
    try:
        role = Role.objects.get(roleId = id)
    except Role.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    role.isActive = False
    serializer = RoleSerializer(role)
    serializer.save()