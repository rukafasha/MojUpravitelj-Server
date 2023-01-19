from django.db import models

class Company(models.Model):
    companyId = models.IntegerField(primary_key=True)
    companyName = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Company"