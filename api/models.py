from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    message = models.CharField(blank=True, max_length=300, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=True, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'massage': self.message,
            'author_id': self.author_id,
            'date': self.date
        }

    class Meta:
        verbose_name = 'Message',
        verbose_name_plural = 'Messages'


# Create your models her
class Country(models.Model):
    name = models.CharField(max_length=300, null=True)
    infected_count = models.IntegerField(default=0, null=True)
    recovered_count = models.IntegerField(default=0, null=True)
    died_count = models.IntegerField(default=0, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'infected_count': self.infected_count,
            'recovered_count': self.recovered_count,
            'died_count': self.died_count
        }

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300, null=True)
    infected_count = models.IntegerField(default=0, null=True)
    recovered_count = models.IntegerField(default=0, null=True)
    died_count = models.IntegerField(default=0, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'country_id': self.country_id,
            'name': self.name,
            'infected_count': self.infected_count,
            'recovered_count': self.recovered_count,
            'died_count': self.died_count
        }

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300, null=True)
    infected_count = models.IntegerField(default=0, null=True)
    recovered_count = models.IntegerField(default=0, null=True)
    died_count = models.IntegerField(default=0, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'country_id': self.country_id,
            'region_id': self.region_id,
            'name': self.name,
            'infected_count': self.infected_count,
            'recovered_count': self.recovered_count,
            'died_count': self.died_count
        }

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Person(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=0)
    is_infected = models.NullBooleanField(blank=True, default=False)
    infected_by = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    infected_date = models.CharField(blank=True, null=True, max_length=300)
    is_recovered = models.NullBooleanField(blank=True, default=False, null=True)
    is_died = models.NullBooleanField(blank=True, default=False, null=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'region_id': self.region,
            'city_id': self.city_id,
            'country_id': self.country_id,
            'is_infected': self.is_infected,
            'infected_by': self.infected_by,
            'infected_date': self.infected_date,
            'is_recovered': self.is_recovered,
            'is_died': self.is_died

        }
