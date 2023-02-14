from django.db import models

from ..Appartment.AppartmentModel import Appartment
from ..Person.PersonModel import Person
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Request(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    requestId = models.AutoField(primary_key=True)
    ownerId = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='owner')
    tenantId = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='tenant')
    appartmentId = models.ForeignKey(Appartment, on_delete=models.CASCADE)
    approved = models.BooleanField(null=True, blank=True)
    
    class Meta:
        db_table = "Request"
