from django.db import models
from ..Person.PersonModel import Person
from ..Role.RoleModel import Role

class RolePerson(models.Model):
    id = models.AutoField(primary_key=True)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

    
    class Meta:
        db_table = "RolePerson"
        unique_together = (('personId', 'roleId'),)
        index_together = (('personId', 'roleId'),)