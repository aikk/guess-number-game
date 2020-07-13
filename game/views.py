from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from random import randint


def game(request):
    games = Game.objects.all()
    return render(request, 'game.html', {'games': games})


def new_game(request):
    if request.method == 'POST':
        if request.POST.get('min_number') and request.POST.get('max_number'):
            game = Game()
            game.min_number = int(request.POST.get('min_number'))
            game.max_number = int(request.POST.get('max_number'))
            game.number = randint(game.min_number, game.max_number)
            game.save()
            return redirect('game_detail', game_id=game.id)
    else:
        return render(request, 'new_game.html')


def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game_detail.html', {'game': game})
