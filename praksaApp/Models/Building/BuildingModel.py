from django.db import models
from ..County.CountyModel import County
from ..Person.PersonModel import Person
from ..Company.CompanyModel import Company

class Building(models.Model):
    buildingId = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=255)
    numberOfAppartment = models.IntegerField()
    countyId = models.ForeignKey(County, on_delete=models.CASCADE)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    representativeId = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, unique=True)
    
    class Meta:
        db_table = "Building"