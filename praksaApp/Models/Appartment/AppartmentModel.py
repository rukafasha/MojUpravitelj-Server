from django.db import models
from ..Building.BuildingModel import Building
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Appartment(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    appartmentId = models.AutoField(primary_key=True)
    appartmentNumber = models.IntegerField()
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)
    numberOfPeople = models.IntegerField()
    
    class Meta:
        db_table = "Appartment"
    def __str__(self):
        return self.buildingId.address + " - " +str(self.appartmentNumber)