from player import Player
from state import State

class Game:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.state = State()

    def reset(self):
        self.currentState = State()

    def play(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.play()        