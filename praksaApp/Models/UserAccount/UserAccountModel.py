from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class UserAccount(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    userAccountId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    approved = models.BooleanField(default=True)
    
    class Meta:
        db_table = "UserAccount"
        
    def __str__(self):
        return self.username