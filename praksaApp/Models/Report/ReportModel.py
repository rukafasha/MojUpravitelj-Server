from django.db import models
from ..Person.PersonModel import Person
from ..Role.RoleModel import Role

class Report(models.Model):
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    
    
    class Meta:
        db_table = "Report"
        unique_together = (('personId', 'roleId'),)