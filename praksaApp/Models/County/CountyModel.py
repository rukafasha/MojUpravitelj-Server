from django.db import models
from ..Country.CountryModel import Country

class County(models.Model):
    countyId = models.IntegerField(primary_key=True)
    countyName = models.CharField(max_length=100)
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "County"