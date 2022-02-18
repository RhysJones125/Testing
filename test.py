from tennis import tennis

def test_player_score_is15_on_round1():
    scored=tennis(1)
    assert scored == 15

def test_player_score_is30_on_round2():
    scored=tennis(2)
    assert scored == 30

def test_player_score_is40_on_round3():
    scored=tennis(3)
    assert scored == 40
