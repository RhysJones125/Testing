from tennis import Game

def test_player_1_scored_returns_15_0():
    game = Game()
    score = game.scored(1)
    assert score == (15,0)

def test_player_2_scored_returns_0_15():
    game = Game()
    score = game.scored(2)
    assert score == (0,15)

def test_player_1_scored_twice_returns_30_0():
    game = Game()
    score = game.scored(1)
    score = game.scored(1)
    assert score == (30,0)