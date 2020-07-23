from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Game, Guess
from random import randint
from .forms import UserForm


class NumberTooHighException(Exception):
    pass


class NumberTooLowException(Exception):
    pass


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
            make_guess(game, guess_value)
        except ValueError:
            return redirect(reverse('error', args=['guess number type incorrect']), request)
        except (NumberTooHighException, NumberTooLowException) as e:
            return redirect(reverse('error', args=[str(e)]), request)

        if game.is_active and game.number == guess_value:
            game.is_active = False
            game.save()
    return render(request, 'game_detail.html', {'game': game, 'guesses': guesses})


def make_guess(game, number):
    if number > game.max_number:
        raise NumberTooHighException('number too high')
    elif number < game.min_number:
        raise NumberTooLowException('number too low')
    else:
        guess = Guess.objects.create(game=game, number=number)
        return guess


def error(request, text):
    return render(request, 'error.html', {'text': text})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        registered = True
    else:
        user_form = UserForm()

    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})
