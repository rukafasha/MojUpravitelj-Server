from django.db import models
from ..Person.PersonModel import Person
from ..Appartment.AppartmentModel import Appartment

class AppartmentPerson(models.Model):
    id = models.AutoField(primary_key=True)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person_rel")
    appartmentId = models.ForeignKey(Appartment, on_delete=models.CASCADE, related_name="appartment_rel")
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "AppartmentPerson"
        unique_together = (('personId', 'appartmentId'))
        index_together = (('personId', 'appartmentId'),)
        