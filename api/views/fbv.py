from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Country, Person, Region, City, Message
from api.serializers import CountrySerializer, PersonSerializer, RegionSerializer, CitySerializer, MessageSerilizer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        Message.objects.create(
            message=request.user.username + " got countries",
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " created new country " + request.data.get('name'),
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        Message.objects.create(
            message=request.user.username + " got cities list ",
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " created new city " + request.data.get("name"),
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def region_list(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        Message.objects.create(
            message=request.user.username + " got regions list ",
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " created new region " + request.data.get('name'),
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def country_detail(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        Message.objects.create(
            message=request.user.username + " got country detail " + country.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " edited country " + country.name,
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        country.delete()
        Message.objects.create(
            message=request.user.username + " deleted country " + country.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response({'deleted': True})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def region_detail(request, region_id):
    try:
        region = Region.objects.get(id=region_id)
    except Region.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        Message.objects.create(
            message=request.user.username + " got region detail " + region.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegionSerializer(instance=region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " edited region " + region.name,
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        region.delete()
        Message.objects.create(
            message=request.user.username + " deleted region " + region.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response({'deleted': True})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def city_detail(request, city_id):
    try:
        city = City.objects.get(id=city_id)
    except City.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CitySerializer(city)
        Message.objects.create(
            message=request.user.username + " got city detail " + city.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CitySerializer(instance=city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " edited city " + city.name,
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        city.delete()
        Message.objects.create(
            message=request.user.username + " deleted city " + city.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response({'deleted': True})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def person_list(request):
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        Message.objects.create(
            message=request.user.username + " got people list ",
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " created person " + request.data.get('name'),
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def message_list_by_user_id(request):
    if request.method == 'GET':
        messages = Message.objects.filter(author_id=request.user.id)
        serializer = MessageSerilizer(messages, many=True)
        return Response(serializer.data)
    pass


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def person_detail(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        Message.objects.create(
            message=request.user.username + " got person detail " + person.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

    elif request.method == 'PUT':
        # if request.data.get('is_died') and not person.is_died:
        #     country_id = request.data.get('country_id')
        #     region_id = request.data.get('region_id')
        #     city_id = request.data.get('city_id')
        #     country = Country.objects.get(id=country_id)
        #     city = City.objects.get(id=city_id)
        #     region = Region.objects.get(id=region_id)
        #     country.died_count+=1
        #     city.died_count+=1
        #     region.died_count+=1
        if request.data.get('is_infected') and not person.is_infected:

            country_id = person.country_id
            region_id = person.region_id
            city_id = person.city_id
            country = Country.objects.get(id=country_id)
            city = City.objects.get(id=city_id)
            region = Region.objects.get(id=region_id)
            city_new = City.objects.get(id=city_id)
            city_new.infected_count = city_new.infected_count + 1
            print(city_new.infected_count)
            ciSerializer = CitySerializer(instance=city,data=city_new)
            if ciSerializer.is_valid():
                print('aaaaaa')
                ciSerializer.save()
        # if request.data.get('is_recovered') and not person.is_recovered:
        #     country_id = request.data.get('country_id')
        #     region_id = request.data.get('region_id')
        #     city_id = request.data.get('city_id')
        #     country = Country.objects.get(id=country_id)
        #     city = City.objects.get(id=city_id)
        #     region = Region.objects.get(id=region_id)
        #     city_new = City.objects.get(id=city_id)
        #     city_new.infected_count = city_new.infected_count + 1
        #     ciSerializer = CitySerializer(instance=city,data=city_new)
        #     if ciSerializer.is_valid():
        #         ciSerializer.save()
        # # if not request.data.get('is_infected') and not person.is_died and person.is_infected:
        #     country_id = request.data.get('country_id')
        #     region_id = request.data.get('region_id')
        #     city_id = request.data.get('city_id')
        #     country = Country.objects.get(id=country_id)
        #     city = City.objects.get(id=city_id)
        #     region = Region.objects.get(id=region_id)
        #     country.infected_count -= 1
        #     city.infected_count -= 1
        #     region.infected_count = 1

        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Message.objects.create(
                message=request.user.username + " edited person detail " + person.name,
                author_id=request.user.id,
                date=datetime.now()
            )
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        person.delete()
        Message.objects.create(
            message=request.user.username + " deleted person detail " + person.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response({'deleted': True})
