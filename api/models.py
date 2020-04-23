from django.db import models


# Create your models her
class Country(models.Model):
    name = models.CharField(max_length=300)
    infected_count = models.IntegerField(default=0)
    recovered_count = models.IntegerField(default=0)
    died_count = models.IntegerField(default=0)

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
    country = models.ForeignKey(Country , on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=300)
    infected_count = models.IntegerField(default=0)
    recovered_count = models.IntegerField(default=0)
    died_count = models.IntegerField(default=0)

    def to_json(self):
        return {
            'id': self.id,
            'coutry_id':self.country_id,
            'name': self.name,
            'infected_count': self.infected_count,
            'recovered_count': self.recovered_count,
            'died_count': self.died_count
        }

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null = True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=300)
    infected_count = models.IntegerField(default=0)
    recovered_count = models.IntegerField(default=0)
    died_count = models.IntegerField(default=0)

    def to_json(self):
        return {
            'id': self.id,
            'country_id':self.country_id,
            'region_id':self.region_id,
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
    infected_date = models.DateField(blank=True, null=True)
    is_recovered = models.NullBooleanField(blank=True, default=False)
    is_died = models.NullBooleanField(blank=True, default=False)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'region_id':self.region,
            'city_id':self.city_id,
            'country_id': self.country_id,
            'is_infected': self.is_infected,
            'infected_by': self.infected_by,
            'infected_date': self.infected_date,
            'is_recovered': self.is_recovered,
            'is_died': self.is_died

        }
