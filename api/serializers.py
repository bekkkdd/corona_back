from rest_framework import serializers
from api.models import Country, Person


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only='True')
    name = serializers.CharField()
    infected_count = serializers.IntegerField()
    recovered_count = serializers.IntegerField()
    died_count = serializers.IntegerField()

    def create(self, validated_data):
        # print("HEllo")
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


class PersonSerializer(serializers.ModelSerializer):
    # country_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'is_infected', 'infected_by', 'country_id' ,'infected_date', 'is_recovered', 'is_died')
