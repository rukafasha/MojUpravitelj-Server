from django.db import models

class ReportStatus(models.Model):
    reportStatusId = models.AutoField(primary_key=True)
    statusDescription = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "ReportStatus"
        
    def __str__(self):
        return str(self.reportStatusId) + " - " + self.statusDescription