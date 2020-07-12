from django.db import models


class Game(models.Model):
    min_number = models.IntegerField()
    max_number = models.IntegerField()
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Guess(models.Model):
    number = models.IntegerField()
    time = models.DateField(auto_now=False, auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
