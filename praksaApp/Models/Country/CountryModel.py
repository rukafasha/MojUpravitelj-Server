from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Country(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    countryId = models.AutoField(primary_key = True)
    countryName = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Country"
        
    def __str__(self):
        return str(self.countryId) + " - " + self.countryName