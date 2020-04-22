from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Country, Person
from api.serializers import CountrySerializer, PersonSerializer


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def country_detail(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        country.delete()
        return Response({'deleted': True})


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def country_people(request, country_id):
    try:
        people = Person.objects.filter(country_id=country_id)
    except Person.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(instance=people, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        people.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def person_list(request):
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def person_detail(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        person.delete()
        return Response({'deleted': True})
