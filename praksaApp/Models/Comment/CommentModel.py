from django.db import models
from ..Person.PersonModel import Person
from ..Report.ReportModel import Report

class Comment(models.Model):
    commentId = models.IntegerField(primary_key=True)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    reportId = models.ForeignKey(Report, on_delete=models.CASCADE)
    content = models.TextField()
    
    class Meta:
        db_table = "Comment"