class Game:
    def __init__(self):
        self.player_one_score = 0
        self.player_two_score = 0

    def scored(self, player):
        if(player == 1):
            self.player_one_score+=15
        elif(player == 2):
            self.player_two_score+=15

        return (self.player_one_score, self.player_two_score)
