from pickle import FALSE
from django.db import models

# Create your models here.

class Bet(models.Model):
    name = models.CharField(max_length=50)
    total_score = models.IntegerField(default=0)
    wager = models.IntegerField()

    def __str__(self):
        return self.name

    

