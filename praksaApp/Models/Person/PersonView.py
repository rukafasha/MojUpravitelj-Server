from praksaApp.Models.AppartmentPerson.AppartmentPersonSerializer import AppartmentPersonSerializer
from praksaApp.Models.AppartmentPerson.AppartmentPersonModel import AppartmentPerson
from .PersonModel import Person
from .PersonSerializer import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def PersonGetAll(request):
    person = Person.objects.all().distinct()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def PersonAdd(request):
    serializer = PersonSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def PersonGetById(request, id):
    try:
        person = Person.objects.get(personId = id)
    except Person.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(person)
    return Response(serializer.data)

@api_view(['PUT'])
def PersonPut(request, id):
    try:
        person = Person.objects.get(personId = id)
    except Person.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(person, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def PersonDelete(request, id):
    try:
        person = Person.objects.get(personId = id).delete()
    except Person.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])  
def GetPersonByAppartment(request, id):
    try:
        appPerson = AppartmentPerson.objects.filter(appartmentId = id)
    except AppartmentPerson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    person = []
    try:
        for apperson in appPerson:
            person.append(apperson.personId)
    except Person.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)