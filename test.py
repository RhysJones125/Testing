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

def test_player_2_scored_twice_returns_0_30():
    game = Game()
    score = game.scored(2)
    score = game.scored(2)
    assert score == (0,30)

def test_both_players_score_returns_15_15():
    game = Game()
    game.scored(1)
    score = game.scored(2)
    assert score == (15,15)

def test_player_1_scores_thrice_returns_40_0():
    game = Game()
    game.scored(1)
    game.scored(1)
    score = game.scored(1)
    assert score == (40, 0)

def test_player_2_scores_thrice_returns_0_40():
    game = Game()
    game.scored(2)
    game.scored(2)
    score = game.scored(2)
    assert score == (0, 40)

def test_player_1_scores_4times_returns_player1_wins():
    game = Game()
    game.scored(1)
    game.scored(1)
    game.scored(1)
    score=game.scored(1)
    assert score=="player 1 wins"

def test_player_2_scores_4times_returns_player2_wins():
    game = Game()
    game.scored(2)
    game.scored(2)
    game.scored(2)
    score=game.scored(2)
    assert score=="player 2 wins"

def test_both_players_score_40_returns_deuce():
    game = Game()
    game.scored(2)
    game.scored(2)
    score=game.scored(2)
    game.scored(1)
    game.scored(1)
    score=game.scored(1)
    assert score=="deuce"

def test_deuce_then_player_1_scores_returns_player1_advantage():
    game = Game()
    game.scored(2)
    game.scored(2)
    game.scored(2)
    game.scored(1)
    game.scored(1)
    game.scored(1)
    score=game.scored(1)
    assert score=="player 1 advantage"

def test_deuce_then_player_2_scores_returns_player2_advantage():
    game = Game()
    game.scored(2)
    game.scored(2)
    game.scored(2)
    game.scored(1)
    game.scored(1)
    game.scored(1)
    score=game.scored(2)
    assert score=="player 2 advantage"