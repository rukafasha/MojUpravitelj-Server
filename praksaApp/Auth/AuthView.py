from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from praksaApp.Auth.AuthSerializer import CompanyRegistrationSerializer, LoginSerializer, RegistrationSerializer
from praksaApp.Models.AppartmentPerson.AppartmentPersonModel import AppartmentPerson
from praksaApp.Models.Building.BuildingModel import Building
from praksaApp.Models.Building.BuildingSerializer import BuildingSerializer
from praksaApp.Models.Company.CompanyModel import Company

from praksaApp.Models.Person.PersonModel import Person
from praksaApp.Models.Person.PersonSerializer import PersonSerializer
from praksaApp.Models.Role.RoleModel import Role
from praksaApp.Models.Role.RoleSerializer import RoleSerializer
from praksaApp.Models.RolePerson.RolePersonModel import RolePerson
from praksaApp.Models.RolePerson.RolePersonSerializer import RolePersonSerializer
from praksaApp.Models.RolePerson.RolePersonView import RoleGetByUser
from praksaApp.Models.UserAccount.UserAccountModel import UserAccount
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def Login(request):
    login_serializer = LoginSerializer(data=request.data)

    if login_serializer.is_valid():
        try:
            user_account = UserAccount.objects.get(username = request.data['username'])        
        except UserAccount.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)

        if user_account.approved:
            if(check_password(request.data['password'], user_account.password)):
            # if(user_account.password == request.data['password']):
                person = Person.objects.get(userAccountId = user_account.userAccountId)
                person_serializer = PersonSerializer(person)

                try:
                    role_person = RolePerson.objects.filter(personId = person.personId)

                    list_of_roles = []

                    for role in role_person:
                        list_of_roles.append(role.roleId.roleName)

                except RolePerson.DoesNotExist:
                    return Response("Role not found.",status = status.HTTP_404_NOT_FOUND)

                building_ids = []

                try:
                    appartment_person_list = AppartmentPerson.objects.filter(personId = person.personId)

                    for app_person in appartment_person_list:
                        building_ids.append(app_person.appartmentId.buildingId.buildingId)
                except AppartmentPerson.DoesNotExist:
                    return Response("Building not found.",status=status.HTTP_404_NOT_FOUND)

                data = {   
                        "person":person_serializer.data, 
                        "building_ids":building_ids,
                        "list_of_roles":list_of_roles
                        }

                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response("Incorrect password. Please try again.", status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            return Response("The owner must approve your request.",status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        return Response("Invalid data received.",status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Registration(request):
    registration_serializer = RegistrationSerializer(data=request.data)

    if registration_serializer.is_valid():
        try:
            user_account = UserAccount.objects.get(username = request.data['username'])
        except UserAccount.DoesNotExist:
            hashed_pwd = make_password(request.data["password"])

            user__id = UserAccount.objects.create(username=request.data['username'], password=hashed_pwd)
            person__id = Person.objects.create(firstName=request.data['firstName'], lastName=request.data['lastName'],dateOfBirth=request.data['dateOfBirth'],userAccountId = user__id)
            
            try:
                tenant_role = Role.objects.get(roleName = "tenant")
                RolePerson.objects.create(personId = person__id, roleId = tenant_role)
            except Role.DoesNotExist:
                return Response("Role not found.",status=status.HTTP_404_NOT_FOUND)

            data = person__id.personId
          
            return Response(data, status=status.HTTP_201_CREATED)
        return Response("Registration failed. The username is already taken.",status=status.HTTP_409_CONFLICT)
    else:
        return Response("Invalid data received.",status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def CompanyRegistration(request):
    company_registration_serializer = CompanyRegistrationSerializer(data=request.data)

    if company_registration_serializer.is_valid():
        try:
            user_account = UserAccount.objects.get(username = request.data['username'])
        except UserAccount.DoesNotExist:
            hashed_pwd = make_password(request.data["password"])
            user__id = UserAccount.objects.create(username=request.data['username'], password=hashed_pwd)
            company__id = Company.objects.create(companyName=request.data['companyName'])
            person__id = Person.objects.create(firstName=request.data['firstName'], lastName=request.data['lastName'],dateOfBirth=request.data['dateOfBirth'],companyId=company__id,userAccountId = user__id)
            
            try:
                company_role = Role.objects.get(roleName = "company")
                RolePerson.objects.create(personId = person__id, roleId = company_role)
            except Role.DoesNotExist:
                return Response("Role not found.",status=status.HTTP_404_NOT_FOUND)

            return Response("Registration Successful.", status=status.HTTP_201_CREATED)
        return Response("Registration failed. The username is already taken.",status=status.HTTP_409_CONFLICT)
    else:
        return Response("Invalid data received.",status=status.HTTP_400_BAD_REQUEST)