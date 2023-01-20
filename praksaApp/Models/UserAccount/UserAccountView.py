from .UserAccountModel import UserAccount
from .UserAccountSerializer import UserAccountSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def UserAccountList(request):
    if request.method == 'GET':
        userAccount = UserAccount.objects.all()
        serializer = UserAccountSerializer(userAccount, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = UserAccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def UserAccountDetail(request, id):
    
    try:
        userAccount = UserAccount.objects.get(userAccountId = id)
    except UserAccount.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserAccountSerializer(userAccount)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserAccountSerializer(userAccount, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        userAccount.isActive = False
        serializer = UserAccountSerializer(userAccount)
        serializer.save()