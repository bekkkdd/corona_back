from rest_framework import serializers
from api.models import Country, Person, City, Region, Message


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only='True')
    name = serializers.CharField()
    infected_count = serializers.IntegerField()
    recovered_count = serializers.IntegerField()
    died_count = serializers.IntegerField()

    def create(self, validated_data):
        country = Country.objects.create(
            name=validated_data.get('name'),
            infected_count=validated_data.get('infected_count'),
            recovered_count=validated_data.get('recovered_count'),
            died_count=validated_data.get('died_count')
        )
        return country

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.infected_count = validated_data.get('infected_count', instance.infected_count)
        instance.recovered_count = validated_data.get('recovered_count', instance.recovered_count)
        instance.died_count = validated_data.get('died_count', instance.died_count)
        instance.save()
        return instance


class RegionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only='True')
    name = serializers.CharField()
    country_id = serializers.IntegerField()
    infected_count = serializers.IntegerField()
    recovered_count = serializers.IntegerField()
    died_count = serializers.IntegerField()

    def create(self, validated_data):
        region = Region.objects.create(
            name=validated_data.get('name'),
            country_id=validated_data.get('country_id'),
            infected_count=validated_data.get('infected_count'),
            recovered_count=validated_data.get('recovered_count'),
            died_count=validated_data.get('died_count')
        )
        return region

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country_id = validated_data.get('country_id', instance.country_id)
        instance.infected_count = validated_data.get('infected_count', instance.infected_count)
        instance.recovered_count = validated_data.get('recovered_count', instance.recovered_count)
        instance.died_count = validated_data.get('died_count', instance.died_count)
        instance.save()
        return instance


class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()

    class Meta:
        model = City
        fields = ('id', 'name', 'country_id', 'region_id', 'infected_count', 'recovered_count', 'died_count')


class PersonSerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    city_id = serializers.IntegerField()
    infected_by_id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = Person
        fields = (
            'id', 'name', 'surname', 'is_infected', 'infected_by_id', 'country_id', 'region_id', 'city_id',
            'infected_date',
            'is_recovered', 'is_died')


class MessageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id', 'message', 'date', 'author_id'
        )
