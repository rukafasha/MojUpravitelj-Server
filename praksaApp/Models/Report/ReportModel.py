from django.db import models
from ..Person.PersonModel import Person
from ..ReportStatus.ReportStatusModel import ReportStatus
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Report(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    timeCreated = models.DateTimeField(auto_now_add=True)
    timeFinished = models.DateTimeField(null=True, blank=True)
    madeBy = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="madeBy")
    closedBy = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name="closedBy", blank=True)
    status = models.ForeignKey(ReportStatus, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Report"
        
    def __str__(self):
        return self.madeBy.firstName + " " + self.madeBy.lastName + " - " + self.title