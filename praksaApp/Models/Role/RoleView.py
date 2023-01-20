from .RoleModel import Role
from .RoleSerializer import RoleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def RoleList(request):
    if request.method == 'GET':
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = RoleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def RoleDetail(request, id):
    
    try:
        roleDetail = Role.objects.get(roleId = id)
    except Role.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RoleSerializer(roleDetail)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = RoleSerializer(roleDetail, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        roleDetail.isActive = False
        serializer = RoleSerializer(roleDetail)
        serializer.save()