from django.db import models

class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "Company"