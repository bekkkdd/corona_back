from datetime import datetime

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Country, Person, Region, City, Message
from api.serializers import CountrySerializer, PersonSerializer, RegionSerializer, CitySerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAuthenticated,)

class RegionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAuthenticated,)


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)


class CountryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)

class CityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)


class PersonDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)


class CountryPeople(APIView):
    def get(self, request, country_id):
        country = Country.objects.get(id = country_id)
        Message.objects.create(
            message=request.user.username + " got people by country " + country.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        people = Person.objects.filter(country_id=country_id)
        # print(people.get(0))
        serializer = PersonSerializer(people, many=True)
        print(serializer.data)
        return Response(serializer.data)


class RegionPeople(APIView):
    def get(self, request, region_id):
        people = Person.objects.filter(region_id=region_id)
        # print(people.get(0))
        serializer = PersonSerializer(people, many=True)
        print(serializer.data)
        region = Region.objects.get(id=region_id)
        Message.objects.create(
            message=request.user.username + " got people by region " + region.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)


class CityPeople(APIView):
    def get(self, request, city_id):
        people = Person.objects.filter(city_id=city_id)
        # print(people.get(0))
        serializer = PersonSerializer(people, many=True)
        print(serializer.data)
        city = City.objects.get(id=city_id)
        Message.objects.create(
            message=request.user.username + " got people by city " + city.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

class CountryRegions(APIView):
    def get(self, request, country_id):
        regions = Region.objects.filter(country_id=country_id)
        # print(regions.get(0))
        serializer = RegionSerializer(regions, many=True)
        print(serializer.data)
        country = Country.objects.get(id=country_id)
        Message.objects.create(
            message=request.user.username + " got regions by country " + country.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

class CountryCities(APIView):
    def get(self, request, country_id):
        cities = City.objects.filter(country_id=country_id)
        # print(cities.get(0))
        serializer = CitySerializer(cities, many=True)
        print(serializer.data)
        country = Country.objects.get(id=country_id)
        Message.objects.create(
            message=request.user.username + " got cities by country " + country.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)

class RegionCities(APIView):
    def get(self, request, region_id):
        cities = City.objects.filter(region_id=region_id)
        # print(cities.get(0))
        serializer = CitySerializer(cities, many=True)
        print(serializer.data)
        region = Region.objects.get(id = region_id)
        Message.objects.create(
            message=request.user.username + " got cities by region " + region.name,
            author_id=request.user.id,
            date=datetime.now()
        )
        return Response(serializer.data)