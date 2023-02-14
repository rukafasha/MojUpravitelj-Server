from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from praksaApp.Models.Request.RequestModel import Request
from praksaApp.Models.Request.RequestSerializer import RequestSerializer


@api_view(['GET'])
def RequestGetAll(request):
    req = Request.objects.all()
    serializer = RequestSerializer(req, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def RequestGetNotApproved(request):
    try:
        req = Request.objects.filter(approved=True)
    except Request.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    print(req)
    serializer = RequestSerializer(req, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def RequestAdd(request):
    serializer = RequestSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def RequestPut(request, id):
    try:
        req = Request.objects.get(requestId = id)
    except Request.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = RequestSerializer(req, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)