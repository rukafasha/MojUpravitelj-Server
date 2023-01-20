from .ReportStatusModel import ReportStatus
from .ReportStatusSerializer import ReportStatusSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def ReportStatusList(request):
    if request.method == 'GET':
        reportStatus = ReportStatus.objects.all()
        serializer = ReportStatusSerializer(reportStatus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ReportStatusSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def ReportStatusDetail(request, id):
    
    try:
        reportStatus = ReportStatus.objects.get(reportStatusId = id)
    except ReportStatus.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReportStatusSerializer(reportStatus)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ReportStatusSerializer(reportStatus, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        reportStatus.isActive = False
        serializer = ReportStatusSerializer(reportStatus)
        serializer.save()
        