from .UserAccountModel import UserAccount
from .UserAccountSerializer import UserAccountSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def UserAccountGetAll(request):
    userAccount = UserAccount.objects.all().distinct()
    serializer = UserAccountSerializer(userAccount, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def UserAccountAdd(request):
    serializer = UserAccountSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def UserAccountGetById(request, id):
    try:
        userAccount = UserAccount.objects.get(userAccountId = id)
    except UserAccount.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = UserAccountSerializer(userAccount)
    return Response(serializer.data)

@api_view(['PUT'])
def UserAccountPut(request, id):
    try:
        userAccount = UserAccount.objects.get(userAccountId = id)
    except UserAccount.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = UserAccountSerializer(userAccount, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def UserAccountDelete(request, id):
    try:
        userAccount = UserAccount.objects.get(userAccountId = id).delete()
    except UserAccount.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def UserAccountUsernameVerification(request, username):
    try:
        UserAccount.objects.get(username = username)
    except UserAccount.DoesNotExist:
        return Response(status = status.HTTP_200_OK)
    return Response(status = status.HTTP_409_CONFLICT)