from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Country, Person
from api.serializers import CountrySerializer, PersonSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # permission_classes = (IsAuthenticated,)


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # permission_classes = (IsAuthenticated,)


class CountryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # permission_classes = (IsAuthenticated,)


class PersonDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # permission_classes = (IsAuthenticated,)


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
