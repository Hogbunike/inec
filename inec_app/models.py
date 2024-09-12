from django.db import models

# Create your models here.
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

class LGA(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Ward(models.Model):
    name = models.CharField(max_length=100)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(unique=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

class AnnouncedPUResult(models.Model):
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party_abbreviation = models.CharField(max_length=3)
    party_score = models.IntegerField()

class AnnouncedLGAResult(models.Model):
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    party_abbreviation = models.CharField(max_length=3)
    party_score = models.IntegerField()