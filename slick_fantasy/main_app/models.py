from pickle import FALSE
from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Bet(models.Model):
    name = models.CharField(max_length=50)
    total_score = models.IntegerField(default=0)
    wager = models.IntegerField()

    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name


