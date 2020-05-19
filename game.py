from player import Player
from state import State

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.state = State()
        self.currentPlayer = None

    def reset(self):
        self.state = State()

    def play(self):
        self.currentPlayer = self.player1
        while self.state.end != True :
            move = self.currentPlayer.move()
            if not self.state.addMove(move):
                continue;
            if self.currentPlayer == self.player1 :
                self.currentPlayer = self.player2
            else :
                self.currentPlayer = self.player1    
            #self.state.isEnd()
            self.state.martinIsEnd()
            self.state.printVector()
        print("--- END ---")
        print("Player "+str(self.state.winner)+" wins")

if __name__ == "__main__":
    game = Game()
    game.play()        
