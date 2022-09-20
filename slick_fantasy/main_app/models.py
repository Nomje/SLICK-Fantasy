from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User

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
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


