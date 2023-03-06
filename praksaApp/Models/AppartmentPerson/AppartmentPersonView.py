from praksaApp.Models.Appartment.AppartmentModel import Appartment
from praksaApp.Models.Appartment.AppartmentSerializer import AppartmentSerializer
from praksaApp.Models.Building.BuildingModel import Building
from praksaApp.Models.Person.PersonModel import Person
from praksaApp.Models.Request.RequestModel import Request
from praksaApp.Models.Role.RoleModel import Role
from praksaApp.Models.RolePerson.RolePersonModel import RolePerson
from praksaApp.Models.UserAccount.UserAccountModel import UserAccount
from .AppartmentPersonModel import AppartmentPerson
from .AppartmentPersonSerializer import AppartmentPersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import credentials, messaging

@api_view(['GET'])
def AppartmentPersonGetAll(request):
    appartmentPerson = AppartmentPerson.objects.all().distinct()
    serializer = AppartmentPersonSerializer(appartmentPerson, many=True)        
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AppartmentPersonAddByTenant(request):

    try:
        has_an_owner = AppartmentPerson.objects.filter(appartmentId = request.data['apartment_id'], isOwner=True).count()
        
        if has_an_owner:
            person_obj = Person.objects.get(personId = request.data['person_id'])
            user_account_status = UserAccount.objects.get(userAccountId = person_obj.userAccountId.userAccountId)

            apt_owner = AppartmentPerson.objects.filter(appartmentId = request.data['apartment_id']).first()

            Request.objects.create(ownerId =  apt_owner.personId, tenantId = person_obj, appartmentId = apt_owner.appartmentId)
            
            useracc = UserAccount.objects.get(userAccountId = apt_owner.personId.userAccountId.userAccountId)
            deviceId = useracc.deviceID
            if(deviceId != None and deviceId != "null"):
                message = messaging.Message(
                    notification = messaging.Notification(
                        title = "New appartment request",
                        body = "You have a new request by" + person_obj.firstName + " " + person_obj.lastName,
                    ),
                    token = deviceId,
                )
                response = messaging.send(message)
            return Response(status=status.HTTP_200_OK)
        else:
            appartment = Appartment.objects.get(appartmentId = request.data['apartment_id'])
            person = Person.objects.get(personId = request.data['person_id'])
            
            tenant_role = Role.objects.get(roleName = "Owner")
            try:
                personRole = RolePerson.objects.get(personId = person.personId, roleId = tenant_role.roleId )
            except RolePerson.DoesNotExist:
                personRole = None
                
            if(personRole == None):
                RolePerson.objects.create(personId = person, roleId = tenant_role)
            
            AppartmentPerson.objects.create(appartmentId=appartment, personId=person, isOwner=True)
            return Response(status=status.HTTP_201_CREATED)

    except AppartmentPerson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

@api_view(['POST'])
def AppartmentPersonAdd(request):

    try:
        has_an_owner = AppartmentPerson.objects.filter(appartmentId = request.data['apartment_id'], isOwner=True).count()
        
        if has_an_owner:
            person_obj = Person.objects.get(personId = request.data['person_id'])
            user_account_status = UserAccount.objects.get(userAccountId = person_obj.userAccountId.userAccountId)

            apt_owner = AppartmentPerson.objects.filter(appartmentId = request.data['apartment_id']).first()

            Request.objects.create(ownerId =  apt_owner.personId, tenantId = person_obj, appartmentId = apt_owner.appartmentId)
            
            user_account_status.approved = False
            user_account_status.save()
            
            useracc = UserAccount.objects.get(userAccountId = apt_owner.personId.userAccountId.userAccountId)
            deviceId = useracc.deviceID
            if(deviceId != None and deviceId != "null"):
                message = messaging.Message(
                    notification = messaging.Notification(
                        title = "New appartment request",
                        body = "You have a new request by" + person_obj.firstName + " " + person_obj.lastName,
                    ),
                    token = deviceId,
                )
                response = messaging.send(message)
            
            return Response("Apartment has an owner. Residency application submitted.",status=status.HTTP_200_OK)
        else:
            appartment = Appartment.objects.get(appartmentId = request.data['apartment_id'])
            person = Person.objects.get(personId = request.data['person_id'])

            tenant_role = Role.objects.get(roleName = "Owner")
            RolePerson.objects.create(personId = person, roleId = tenant_role)

            AppartmentPerson.objects.create(appartmentId=appartment, personId=person, isOwner=True)
            return Response(status=status.HTTP_201_CREATED)

    except AppartmentPerson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def AppartmentHasOwner(request):
    try:
        has_an_owner = AppartmentPerson.objects.filter(appartmentId = request.data['apartment_id'], isOwner=True).count()

        if has_an_owner:
            return Response("The apartment has an owner. Would you like to become a tenant?", status=status.HTTP_200_OK)
        else:
            return Response("The apartment doesn't have an owner. Would you like to become the owner of the apartment?", status=status.HTTP_200_OK)
    except AppartmentPerson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def AppartmentPersonGetById(request, id):
    try:
        appartmentPerson = AppartmentPerson.objects.get(id = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = AppartmentPersonSerializer(appartmentPerson)        
    return Response(serializer.data)

@api_view(['PUT'])
def AppartmentPersonPut(request, id):
    try:
        appartmentPerson = AppartmentPerson.objects.get(appartmentPersonId = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = AppartmentPersonSerializer(appartmentPerson, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def AppartmentPersonDelete(request, id):
    try:
        appartmentPerson = AppartmentPerson.objects.get(appartmentPersonId = id).delete()
    except AppartmentPerson.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def GetApartmentsByBuildingId(request, id):
    try:
        apartments = Appartment.objects.filter(buildingId = id)
          
    except Building.DoesNotExist:
        return Response("Apartments not found.",status=status.HTTP_404_NOT_FOUND)

    apartment_details = []

    for apartment in apartments:
        apartment_details.append({
            "apartmentId":apartment.appartmentId,
            "apartmentNumber":apartment.appartmentNumber,
            "buildingId":apartment.buildingId.buildingId,
            "address":apartment.buildingId.address
            })
    
    return Response(apartment_details)

@api_view(['GET'])
def GetApartmentsByPersonId(request, id):
    try:
        apartments = AppartmentPerson.objects.filter(personId = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AppartmentPersonSerializer(apartments, many=True)
    return Response(serializer.data)
