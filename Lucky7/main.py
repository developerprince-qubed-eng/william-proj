import random

class Game():
    def __init__(self):
        self.val = []
    def startBalance(self, balance):
        return balance
    def gameOn(self, balance):
        randNum = random.randint(1, 6)
        randNum2 = random.randint(1, 6)

        if ((randNum + randNum2) % 7== 0):
            balint = int(balance)
            balint = balint + 4
            return balint
        else :
            balint = int(balance)
            balint = balint - 1
            return balint 



game = Game()

bal = input()

out = game.gameOn(bal)

print(out)

