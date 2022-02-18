class Game:
    def __init__(self):
        self.player_one_score = 0
        self.player_two_score = 0

    def scored(self, player):
        if(player == 1):
            return (15,0)
        return True

