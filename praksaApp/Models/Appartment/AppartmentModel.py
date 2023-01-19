from django.db import models
from ..Building.BuildingModel import Building

class Appartment(models.Model):
    appartmentId = models.IntegerField(primary_key=True)
    appartmentNumber = models.IntegerField()
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)
    numberOfPeople = models.IntegerField()
    
    class Meta:
        db_table = "Appartment"