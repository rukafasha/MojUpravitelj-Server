from .CompanyModel import Company
from .CompanySerializer import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def CompanyGetAll(request):
    company = Company.objects.all().distinct()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def CompanyAdd(request):
    serializer = CompanySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def CompanyGetByID(request, id):
    try:
        company = Company.objects.get(companyId = id)
    except Company.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
@api_view(['PUT'])
def CompanyPut(request, id):
    try:
        company = Company.objects.get(companyId = id)
    except Company.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = CompanySerializer(company, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def CompanyDelete(request, id):
    try:
        company = Company.objects.get(companyId = id).delete()
    except Company.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
