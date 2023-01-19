from django.db import models

class UserAccount(models.Model):
    userAccountId = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = "UserAccount"