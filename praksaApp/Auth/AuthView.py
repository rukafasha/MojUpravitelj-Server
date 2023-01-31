from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from praksaApp.Models.Building.BuildingModel import Building
from praksaApp.Models.Building.BuildingSerializer import BuildingSerializer

from praksaApp.Models.Person.PersonModel import Person
from praksaApp.Models.Person.PersonSerializer import PersonSerializer
from praksaApp.Models.Role.RoleModel import Role
from praksaApp.Models.Role.RoleSerializer import RoleSerializer
from praksaApp.Models.RolePerson.RolePersonModel import RolePerson
from praksaApp.Models.RolePerson.RolePersonSerializer import RolePersonSerializer
from praksaApp.Models.RolePerson.RolePersonView import RoleGetByUser
from praksaApp.Models.UserAccount.UserAccountModel import UserAccount

@api_view(['POST'])
def Login(request):      
    try:
        user_account = UserAccount.objects.get(username = request.data['username'])        
    except UserAccount.DoesNotExist:
        return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)

    if(user_account.password == request.data['password']):
        person = Person.objects.get(userAccountId = user_account.userAccountId)
        person_serializer = PersonSerializer(person)
        print(person_serializer.data) 

        try:
            role_person = RolePerson.objects.filter(personId = person.personId)

            list_of_roles = []

            for role in role_person:
                list_of_roles.append(role.roleId.roleName)

        except RolePerson.DoesNotExist:
            return Response("The role of a person does not exist",status = status.HTTP_404_NOT_FOUND)
    

        try:
            building = Building.objects.get(building_rel__appartment_rel__personId = person.personId)

            building_serializer = BuildingSerializer(building)
        except Building.DoesNotExist:
            return Response("The building does not exist",status=status.HTTP_404_NOT_FOUND)

        data = {   
                "person":person_serializer.data, 
                "building":building_serializer.data,
                "list_of_roles":list_of_roles
                }

        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response("The Password You Entered Is Incorrect Please Try Again", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def Registration(request):       
    try:
        person = UserAccount.objects.get(username = request.data['username'])
    except UserAccount.DoesNotExist:
        user__id = UserAccount.objects.create(username=request.data['username'], password=request.data['password'])

        Person.objects.create(firstName=request.data['firstName'], lastName=request.data['lastName'],dateOfBirth=request.data['dateOfBirth'],userAccountId = user__id)
        return Response("Successful registration.", status=status.HTTP_201_CREATED)
    
    return Response("Unsuccessful registration. Username is already registered",status=status.HTTP_409_CONFLICT)
