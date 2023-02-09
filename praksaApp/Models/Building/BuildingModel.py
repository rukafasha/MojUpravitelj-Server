from django.db import models
from ..County.CountyModel import County
from ..Person.PersonModel import Person
from ..Company.CompanyModel import Company
from safedelete.models import SafeDeleteModel, SOFT_DELETE


class Building(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    buildingId = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    numberOfAppartment = models.IntegerField()
    countyId = models.ForeignKey(County, on_delete=models.CASCADE)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    representativeId = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, unique=True, blank=True)
    
    class Meta:
        db_table = "Building"
    def __str__(self):
        return self.address