from django.db import models

# Create your models her
class Country(models.Model):
    name = models.CharField(max_length=300)
    infected_count = models.IntegerField()
    recovered_count = models.IntegerField()
    died_count = models.IntegerField()

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'infected_count':self.infected_count,
            'recovered_count':self.recovered_count,
            'died_count':self.died_count
        }

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Person(models.Model):

    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE,default="0")
    is_infected = models.BooleanField()
    infected_by = models.ForeignKey('self',on_delete=models.CASCADE,default="0")
    infected_date = models.DateField()
    is_recovered = models.BooleanField()
    is_died =  models.BooleanField()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'surname':self.surname,
            'country_id':self.country_id,
            'is_infected':self.is_infected,
            'infected_by':self.infected_by,
            'infected_date':self.infected_date,
            'is_recovered':self.is_recovered,
            'is_died':self.is_died

        }

