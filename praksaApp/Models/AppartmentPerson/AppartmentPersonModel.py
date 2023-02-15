from django.db import models
from ..Person.PersonModel import Person
from ..Appartment.AppartmentModel import Appartment
from safedelete.models import SafeDeleteModel, SOFT_DELETE


class AppartmentPerson(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    id = models.AutoField(primary_key=True)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    appartmentId = models.ForeignKey(Appartment, on_delete=models.CASCADE)
    isOwner = models.BooleanField(default=False)
    
    class Meta:
        db_table = "AppartmentPerson"
        unique_together = (('personId', 'appartmentId'))
        index_together = (('personId', 'appartmentId'),)
        
    def __str__(self):
        return self.personId.firstName + " " + self.personId.lastName + " - " + str(self.appartmentId.appartmentNumber)