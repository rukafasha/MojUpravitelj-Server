from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from praksaApp.Models.Person.PersonModel import Person
from praksaApp.Models.UserAccount.UserAccountModel import UserAccount



@api_view(['POST'])
def Registration(request):       
    try:
        person = UserAccount.objects.get(username = request.data['username'])
    except UserAccount.DoesNotExist:
        user__id = UserAccount.objects.create(username=request.data['username'], password=request.data['password'])

        Person.objects.create(firstName=request.data['firstName'], lastName=request.data['lastName'],dateOfBirth=request.data['dateOfBirth'],userAccountId = user__id)
        return Response("Successful registration.", status=status.HTTP_201_CREATED)
    
    return Response("Unsuccessful registration. Username is already registered",status=status.HTTP_400_BAD_REQUEST)
