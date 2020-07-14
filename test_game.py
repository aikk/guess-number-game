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
    assert 5 <= game.number <= 10
    assert str(game.id) in driver.current_url


def test_guess_correct(live_server, driver, default_games):
    driver.get(live_server.url + '/' + str(default_games[0].id) + '/')
    element = driver.find_element_by_css_selector('[data-test="guess_number"]')
    element.send_keys(7)
    element1 = driver.find_element_by_css_selector('[data-test="submit"]')
    element1.click()
    # assert not default_games[0].is_active
    is_over = driver.find_element_by_css_selector('[data-test="is_over"]')
    assert is_over.text == 'The game is over.'


def test_guess_incorrect(live_server, driver, default_games):
    driver.get(live_server.url + '/' + str(default_games[0].id) + '/')
    element = driver.find_element_by_css_selector('[data-test="guess_number"]')
    element.send_keys(8)
    element1 = driver.find_element_by_css_selector('[data-test="submit"]')
    element1.click()
    assert default_games[0].is_active


# def test_guess_is_not_int(live_server, driver, default_games):
#     driver.get(live_server.url + '/' + str(default_games[0].id) + '/')
#     element = driver.find_element_by_css_selector('[data-test="guess_number"]')
#     element.send_keys('hello')
#     element1 = driver.find_element_by_css_selector('[data-test="submit"]')
#     element1.click()
#     assert 'error' in driver.current_url


# def test_guess_is_out_of_range(live_server, driver, default_games):
#     driver.get(live_server.url + '/1/')

#     guess_number = driver.find_element_by_css_selector('[data-test="guess_number"]')
#     button_make_guess = driver.find_element_by_css_selector('[data-test="submit"]')

#     guess_number.send_keys(1000)

#     button_make_guess.click()
#     assert 'error' in driver.current_url
