from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from praksaApp.Models.Appartment.AppartmentModel import Appartment
from praksaApp.Models.AppartmentPerson.AppartmentPersonModel import AppartmentPerson
from praksaApp.Models.Person.PersonModel import Person

from praksaApp.Models.Request.RequestModel import Request
from praksaApp.Models.Request.RequestSerializer import RequestSerializer
from praksaApp.Models.UserAccount.UserAccountModel import UserAccount


@api_view(['GET'])
def RequestGetAll(request):
    requests = Request.objects.all()

    request_details = []

    for req in requests:
        request_details.append({
            "requestId":req.requestId,
            "ownerId":req.ownerId.personId,
            "tenantId":req.tenantId.personId,
            "appartmentId":req.appartmentId.appartmentId,
            "approved":req.approved,
            "firstName":req.tenantId.firstName,
            "lastName":req.tenantId.lastName,
            "county":req.appartmentId.buildingId.countyId.countyName,
            "country":req.appartmentId.buildingId.countyId.countryId.countryName,
            })
        
    return Response(request_details, status=status.HTTP_200_OK)


@api_view(['GET'])
def RequestGetNotApproved(request, id):
    try:
        requests = Request.objects.filter(ownerId=id, approved=None)
    except Request.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    request_details = []

    for req in requests:
        request_details.append({
            "requestId":req.requestId,
            "ownerId":req.ownerId.personId,
            "tenantId":req.tenantId.personId,
            "appartmentId":req.appartmentId.appartmentId,
            "approved":req.approved,
            "firstName":req.tenantId.firstName,
            "lastName":req.tenantId.lastName,
            "address":req.appartmentId.buildingId.address,
            "county":req.appartmentId.buildingId.countyId.countyName,
            "country":req.appartmentId.buildingId.countyId.countryId.countryName,
            })
        
    return Response(request_details, status=status.HTTP_200_OK)


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
        
        if request.data['approved'] == True:
            person_obj = Person.objects.get(personId = request.data['tenantId'])
            user_account_status = UserAccount.objects.get(userAccountId = person_obj.userAccountId.userAccountId)

            user_account_status.approved = True
            user_account_status.save()

            appartment = Appartment.objects.get(appartmentId = request.data['appartmentId'])
            person = Person.objects.get(personId = request.data['tenantId'])
            AppartmentPerson.objects.create(appartmentId=appartment, personId=person, isOwner=False)
        
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)