import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from game.models import Game


@pytest.yield_fixture(scope="session")
def driver():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        with webdriver.Chrome(chrome_options=chrome_options) as driver:
            yield driver
    else:
        with webdriver.Chrome() as driver:
            yield driver


@pytest.fixture()
def default_games():
    game1 = Game.objects.create(min_number=5, max_number=10, number=7)
    game2 = Game.objects.create(min_number=15, max_number=25, number=17)
    game3 = Game.objects.create(min_number=25, max_number=105, number=50)
    games = [game1, game2, game3]

    return games
