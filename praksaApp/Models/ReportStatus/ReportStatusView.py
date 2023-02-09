from .ReportStatusModel import ReportStatus
from .ReportStatusSerializer import ReportStatusSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def ReportStatusGetAll(request):
    reportStatus = ReportStatus.objects.all().distinct()
    serializer = ReportStatusSerializer(reportStatus, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def ReportStatusAdd(request):
    serializer = ReportStatusSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def ReportStatusGetById(request, id):
    try:
        reportStatus = ReportStatus.objects.get(reportStatusId = id)
    except ReportStatus.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = ReportStatusSerializer(reportStatus)
    return Response(serializer.data)

@api_view(['PUT'])
def ReportStatusPut(request, id):
    try:
        reportStatus = ReportStatus.objects.get(reportStatusId = id)
    except ReportStatus.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = ReportStatusSerializer(reportStatus, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def ReportStatusDelete(request, id):
    try:
        reportStatus = ReportStatus.objects.get(reportStatusId = id).delete()
    except ReportStatus.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


        