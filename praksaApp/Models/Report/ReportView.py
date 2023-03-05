from praksaApp.Models.Company.CompanyModel import Company
from praksaApp.Models.UserAccount.UserAccountModel import UserAccount
from ..AppartmentPerson.AppartmentPersonModel import AppartmentPerson
from..Building.BuildingModel import Building
from .ReportModel import Report
from .ReportSerializer import ReportSerializer
from ..Person.PersonModel import Person
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import credentials, messaging


@api_view(['GET'])
def ReportGetAll(request):
    report = Report.objects.all().distinct()
    serializer = ReportSerializer(report, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def ReportAdd(request):
    serializer = ReportSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        
        userId = request.data["madeBy"]
        
        #get buildings of user
        building_ids = []
        company_Ids = []
        try:
            appartment_person_list = AppartmentPerson.objects.filter(personId_id = userId)
            for app_person in appartment_person_list:
                building_ids.append(app_person.appartmentId.buildingId.buildingId)
                if app_person.appartmentId.buildingId.companyId.companyId not in company_Ids:
                    company_Ids.append(app_person.appartmentId.buildingId.companyId.companyId)
        except AppartmentPerson.DoesNotExist:
            return Response("Building not found.",status=status.HTTP_404_NOT_FOUND)

        
        #get representatives
        representative_ids = []
        try:
            buildings = Building.objects.filter(buildingId__in = building_ids)
            for item in buildings:
                if(item.representativeId != None):
                    representative_ids.append(item.representativeId.personId)
        except Building.DoesNotExist:
            return Response("Building not found",status=status.HTTP_404_NOT_FOUND)
        
        person = Person.objects.filter(personId__in = representative_ids)
        useracc = UserAccount.objects.filter(userAccountId__in = person)
        companyPerson = Person.objects.filter(companyId__in = company_Ids)
        companyUserAcc = UserAccount.objects.filter(userAccountId__in = companyPerson)
        
        #representative zgrade i companija
        tokens = []
        for item in useracc:
            tokens.append(item.deviceID)
        for item in companyUserAcc:
            tokens.append(item.deviceID)
            
        for item in tokens:
            message = messaging.Message(
                notification = messaging.Notification(
                    title = "New report",
                    body = "New report has been made.",
                ),
                token = item,
            )
        response = messaging.send(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def ReportGetById(request, id):
    try:
        report = Report.objects.get(id = id)
    except Report.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = ReportSerializer(report)
    return Response(serializer.data)


@api_view(['PUT'])
def ReportPut(request, id): 
    try:
        report = Report.objects.get(id = id)
    except Report.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = ReportSerializer(report, data = request.data)
    if serializer.is_valid():
        serializer.save()
        
        personId = request.data["madeBy"]
        person = Person.objects.get(personId = personId)
        useracc = UserAccount.objects.get(userAccountId = person.userAccountId.userAccountId)
        deviceId = useracc.deviceID
        message = messaging.Message(
            notification = messaging.Notification(
                title = "Report has been updated",
                body = "Your report has been updated by " + person.firstName + " " + person.lastName,
            ),
            token = deviceId,
        )
        response = messaging.send(message)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def ReportDelete(request, id):
    try:
        report = Report.objects.get(id = id).delete()
    except Report.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def ReportGetByUser(request, id):
    try:
        report = Report.objects.filter(madeBy_id = id).order_by("-timeCreated").distinct()
    except Report.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = ReportSerializer(report, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ReportGetByCompany(request):
    if(request.data["filter"] == "all"):
        try:
            report = Report.objects.filter(madeBy__appartmentperson__appartmentId__buildingId__companyId__companyId = request.data["lista"]).order_by("-timeCreated").distinct()
        except Report.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        try:
            report = Report.objects.filter(madeBy__appartmentperson__appartmentId__buildingId__companyId__companyId = request.data["lista"], status__statusDescription=request.data["filter"]).order_by("-timeCreated").distinct()
        except Report.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ReportSerializer(report, many=True)
    return Response(serializer.data)
        
        
@api_view(['POST'])
def ReportGetByBuilding(request):
    if(request.data["filter"] == "all"):
        try:
            report = Report.objects.filter(madeBy__appartmentperson__appartmentId__buildingId__buildingId__in = request.data["lista"]).order_by("-timeCreated").distinct()
        except Report.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        try:
            report = Report.objects.filter(madeBy__appartmentperson__appartmentId__buildingId__buildingId__in = request.data["lista"], status__statusDescription=request.data["filter"]).order_by("-timeCreated").distinct()
        except Report.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ReportSerializer(report, many=True)
    return Response(serializer.data) 