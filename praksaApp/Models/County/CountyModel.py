from django.db import models
from ..Country.CountryModel import Country
from safedelete.models import SafeDeleteModel, SOFT_DELETE


class County(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    countyId = models.AutoField(primary_key=True)
    countyName = models.CharField(max_length=100)
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "County"
        
    def __str__(self):
        return str(self.countyId) + " - " + self.countryId.countryName + " - " + self.countyName