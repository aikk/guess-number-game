from django.shortcuts import render
from .models import Game


def game(request):
    games = Game.objects.all()
    return render(request, 'game.html', {'games': games})
