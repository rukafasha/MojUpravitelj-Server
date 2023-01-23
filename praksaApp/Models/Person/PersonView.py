from .PersonModel import Person
from .PersonSerializer import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def PersonGetAll(request):
    person = Person.objects.all()
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
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def PersonDelete(request, id):
    try:
        person = Person.objects.get(personId = id)
    except Person.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    person.isActive = False
    serializer = PersonSerializer(person)
    serializer.save()