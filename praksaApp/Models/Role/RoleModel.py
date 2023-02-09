from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Role(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    roleId = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=100)
    roleDescription = models.TextField()

    
    class Meta:
        db_table = "Role"
        
    def __str__(self):
        return str(self.roleId) + " - " + self.roleName