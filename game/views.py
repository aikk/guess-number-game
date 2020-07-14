from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Game, Guess
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
    guesses = game.guess_set.all()

    if request.method == 'POST':
        try:
            guess_value = int(request.POST['guess_number'])
            make_guess(game.id, guess_value)
        except:
            return redirect(reverse('error', args=['guess number type incorrect']), request)

        if game.is_active and game.number == guess_value:
            game.is_active = False
            game.save()
    return render(request, 'game_detail.html', {'game': game, 'guesses': guesses})


def make_guess(game_id, number):
    guess = Guess.objects.create(game_id=game_id, number=number)
    return guess


def error(request, text):
    return render(request, 'error.html', {'text': text})
