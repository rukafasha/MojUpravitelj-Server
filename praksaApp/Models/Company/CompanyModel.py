from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Company(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Company"
        
    def __str__(self):
        return self.companyName