from .CompanyModel import Company
from .CompanySerializer import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def CompanyList(request):
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def CompanyDetail(request, id):
    
    try:
        company = Company.objects.get(countryId = id)
    except Company.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CompanySerializer(company, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        company.isActive = False
        serializer = CompanySerializer(company)
        serializer.save()
        