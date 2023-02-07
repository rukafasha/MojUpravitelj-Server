from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class ReportStatus(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    reportStatusId = models.AutoField(primary_key=True)
    statusDescription = models.CharField(max_length=255)
    
    class Meta:
        db_table = "ReportStatus"
        
    def __str__(self):
        return str(self.reportStatusId) + " - " + self.statusDescription