from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from praksaApp.Models.UserAccount.UserAccountModel import UserAccount

@api_view(['POST'])
def Login(request):      
    try:
        person = UserAccount.objects.get(username = request.data['username'])
    except UserAccount.DoesNotExist:
        return Response("User does not exist", status=status.HTTP_400_BAD_REQUEST)
   

    try:
        person = UserAccount.objects.get(username = request.data['username'], password = request.data['password'])
    except UserAccount.DoesNotExist:
        return Response("The Password You Entered Is Incorrect Please Try Again", status=status.HTTP_400_BAD_REQUEST)

    return Response("You are successfully logged in", status=status.HTTP_200_OK)
