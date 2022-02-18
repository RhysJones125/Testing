class Game:
    def __init__(self):
        self.player_one_score = 0
        self.player_two_score = 0

    def scored(self, player):
        if(player == 1):
            if self.player_one_score < 30:
                self.player_one_score+=15
            elif self.player_one_score < 40:
                self.player_one_score+=10
            else:
                return "player 1 wins"
        elif(player == 2):
            if self.player_two_score<30:
                self.player_two_score+=15
            elif self.player_two_score < 40:
                self.player_two_score+=10
            else:
                return "player 2 wins"
        if(self.player_one_score==40 and self.player_two_score==40):
            return "deuce"

        return (self.player_one_score, self.player_two_score)
