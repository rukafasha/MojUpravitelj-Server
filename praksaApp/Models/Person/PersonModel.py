from django.db import models
from ..Company.CompanyModel import Company
from ..UserAccount.UserAccountModel import UserAccount

class Person(models.Model):
    personId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    userAccountId = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "Person"