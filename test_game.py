def test_index_page(live_server, driver, default_games):
    driver.get(live_server.url)
    link = driver.find_element_by_css_selector('[data-test="new_game_link"]')
    games = driver.find_elements_by_css_selector('[data-test="current_game"]')

    assert link.text == 'Click me!'
    assert len(default_games) == len(games)
