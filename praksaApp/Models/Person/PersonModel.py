from django.db import models
from ..Company.CompanyModel import Company
from ..UserAccount.UserAccountModel import UserAccount
from safedelete.models import SafeDeleteModel, SOFT_DELETE


class Person(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    personId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    userAccountId = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Person"
        
    def __str__(self):
        return self.firstName + " " + self.lastName