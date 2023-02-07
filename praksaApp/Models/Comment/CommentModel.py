from django.db import models
from ..Person.PersonModel import Person
from ..Report.ReportModel import Report

class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    reportId = models.ForeignKey(Report, on_delete=models.CASCADE)
    content = models.TextField()
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "Comment"
        
    def __str__(self):
        return self.personId.firstName + " " + self.personId.lastName + " - " + self.content