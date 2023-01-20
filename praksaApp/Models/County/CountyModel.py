from django.db import models
from ..Country.CountryModel import Country

class County(models.Model):
    countyId = models.AutoField(primary_key=True)
    countyName = models.CharField(max_length=100)
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "County"