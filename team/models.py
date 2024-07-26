from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Team(models.Model):

    name = models.CharField(max_length=100)
    wins = models.IntegerField()
    losses = models.IntegerField()
    division = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.division} - {self.conference} - Wins: {self.wins}, Losses: {self.losses}"

nfl_teams = [
    "Cardinals",
    "Falcons",
    "Ravens",
    "Bills",
    "Panthers",
    "Bears",
    "Bengals",
    "Browns",
    "Cowboys",
    "Broncos",
    "Lions",
    "Packers",
    "Texans",
    "Colts",
    "Jaguars",
    "Chiefs",
    "Raiders",
    "Chargers",
    "Rams",
    "Dolphins",
    "Vikings",
    "Patriots",
    "Saints",
    "Giants",
    "Jets",
    "Eagles",
    "Steelers",
    "49ers",
    "Seahawks",
    "Buccaneers",
    "Titans",
    "Commanders"
]
