class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_game(self):
        if self.player1.choice == self.player2.choice:
            return None
        choices = {self.player1.choice: self.player1.name, self.player2.choice: self.player2.name}
        if "rock" in choices and "scissors" in choices:
            return choices["rock"]
        if "scissors" in choices and "paper" in choices:
            return choices["scissors"]
        if "paper" in choices and "rock" in choices:
            return choices["paper"]