class GameScore:
    def __init__(self):
        self.scores = {}

    def add_score(self, player, points):
        if player not in self.scores:
            self.scores[player] = 0
        self.scores[player] += points

    def subtract_score(self, player, points):
        if player in self.scores:
            self.scores[player] -= points

    def get_winner(self):
        if len(self.scores) == 0:
            print("Гравців ще немає")
            return
        winner = max(self.scores, key=self.scores.get)
        print("Переможець:", winner, "з", self.scores[winner], "очками")

game = GameScore()
game.add_score("Оля", 10)
game.add_score("Ігор", 15)
game.subtract_score("Оля", 3)

print("Результати:")
print(game.scores)

game.get_winner()
