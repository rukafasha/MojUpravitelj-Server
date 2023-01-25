from django.db import models
from ..Person.PersonModel import Person
from ..ReportStatus.ReportStatusModel import ReportStatus

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    timeCreated = models.DateTimeField(auto_now_add=True)
    timeFinished = models.DateTimeField(auto_now_add=True, null=True)
    madeBy = models.ForeignKey(Person, on_delete=models.CASCADE)
    closedBy = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(ReportStatus, on_delete=models.CASCADE)
    isActive = models.BooleanField()
    
    class Meta:
        db_table = "Report"
        unique_together = (('personId', 'roleId'),)