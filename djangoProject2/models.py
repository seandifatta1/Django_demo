from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=100)
    wins = models.IntegerField()
    losses = models.IntegerField()
    division = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=255)
