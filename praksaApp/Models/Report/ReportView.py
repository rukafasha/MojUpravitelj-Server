from .ReportModel import Report
from .ReportSerializer import ReportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def ReportList(request):
    if request.method == 'GET':
        report = Report.objects.all()
        serializer = ReportSerializer(report, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ReportSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def ReportDetail(request, id):
    
    try:
        report = Report.objects.get(reportId = id)
    except Report.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ReportSerializer(report, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        report.isActive = False
        serializer = ReportSerializer(report)
        serializer.save()
        