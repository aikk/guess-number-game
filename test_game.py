from game.models import Game


def test_index_page(live_server, driver, default_games):
    driver.get(live_server.url)
    link = driver.find_element_by_css_selector('[data-test="new_game_link"]')
    games = driver.find_elements_by_css_selector('[data-test="current_game"]')

    assert link.text == 'Click me!'
    assert len(default_games) == len(games)


def test_new_game_create(live_server, driver):
    driver.get(live_server.url + '/new_game/')
    max_num = driver.find_element_by_css_selector('[data-test="max_number"]')
    max_num.send_keys(10)
    min_num = driver.find_element_by_css_selector('[data-test="min_number"]')
    min_num.send_keys(5)
    element = driver.find_element_by_css_selector('[data-test="go_ahead"]')
    element.click()
    game = Game.objects.last()
    assert 5 == game.min_number
    assert 10 == game.max_number
    assert 5 <= game.number < 10
    assert str(game.id) in driver.current_url


# def test_guess_correct(live_server, driver, default_games):
#     driver.get(live_server.url + 'game_detail' + str(default_games[0].id))
#     element = driver.find_element_by_css_selector('[data-test="guess"]')
#     element.send_keys(7)
#     element1 = driver.find_element_by_css_selector('[data-test="guess_submit"]')
#     element1.click()
#     assert not default_games[0].is_active
