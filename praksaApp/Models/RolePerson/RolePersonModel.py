from django.db import models
from ..Person.PersonModel import Person
from ..Role.RoleModel import Role
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class RolePerson(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    id = models.AutoField(primary_key=True)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)

    
    class Meta:
        db_table = "RolePerson"
        unique_together = (('personId', 'roleId'),)
        index_together = (('personId', 'roleId'),)
        
    def __str__(self):
        return self.personId.firstName + " " + self.personId.lastName + " - " + self.roleId.roleName