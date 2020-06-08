from player import Player, Bot
from state import State

class Game:
    def __init__(self, p1 = Player(), p2 =Player()):
        self.player1 = p1
        self.player2 = p2
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

    def train_play(self):
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

    def train(self, epochs=20000):
        player1Win = 0.0
        player2Win = 0.0
        for i in range(0, epochs):
            print("Epoch", i)
            self.play()
            if self.state.winner == 1:
                player1Win += 1
            if self.state.winner  == 2:
                player2Win += 1
            self.reset()
        print(player1Win / epochs)
        print(player2Win / epochs)
        # player1.savePolicy()
        # player2.savePolicy()

if __name__ == "__main__":
    b1 = Bot()
    b2 = Bot()
    game = Game(b1,b2)
    game.train()
    game.play()        
