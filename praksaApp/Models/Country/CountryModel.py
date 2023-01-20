from django.db import models

class Country(models.Model):
    countryId = models.AutoField(primary_key = True)
    countryName = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "Country"