from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Country, Person, Region, City
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
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        people = Person.objects.filter(country_id=country_id)
        # print(people.get(0))
        serializer = PersonSerializer(people, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegionPeople(APIView):
    def get(self, request, region_id):
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        people = Person.objects.filter(region_id=region_id)
        # print(people.get(0))
        serializer = PersonSerializer(people, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CityPeople(APIView):
    def get(self, request, city_id):
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        people = Person.objects.filter(city_id=city_id)
        # print(people.get(0))
        serializer = PersonSerializer(people, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CountryRegions(APIView):
    def get(self, request, country_id):
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        regions = Region.objects.filter(country_id=country_id)
        # print(regions.get(0))
        serializer = RegionSerializer(regions, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CountryCities(APIView):
    def get(self, request, country_id):
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        cities = City.objects.filter(country_id=country_id)
        # print(cities.get(0))
        serializer = CitySerializer(cities, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegionCities(APIView):
    def get(self, request, region_id):
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        cities = City.objects.filter(region_id=region_id)
        # print(cities.get(0))
        serializer = CitySerializer(cities, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
