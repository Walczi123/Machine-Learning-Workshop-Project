from player import Player, Bot
from state import State

class Game:
    def __init__(self, p1 = Player(), p2 =Player(), need_for_win = 3, debug = False):
        self.player1 = p1
        self.player2 = p2
        self.state = State(need_for_win)
        self.need_for_win = need_for_win
        self.currentPlayer = None
        self.debug = debug

    def reset(self):
        self.state = State(self.need_for_win)

    def play(self):
        self.currentPlayer = self.player1
        label = "X"
        while self.state.end != True :
            move = self.currentPlayer.move(self.state)
            if not self.state.addMove((move[0],move[1],label)):
                continue
            if self.currentPlayer == self.player1 :
                self.currentPlayer = self.player2
                label = "O"
            else :
                self.currentPlayer = self.player1  
                label = "X"  
            self.state.isEnd()
            if(self.debug):
                self.state.printVector()
        if(self.debug):
            print("--- END ---")
            print("Player "+str(self.state.winner)+" wins")

    def train(self, iterations=20000):
        player1Win = 0.0
        player2Win = 0.0
        for i in range(0, iterations):
            print("Epoch", i/iterations)
            self.play()
            if self.state.winner == 1:
                player1Win += 1
            if self.state.winner  == 2:
                player2Win += 1
            self.reset()
        print(player1Win / iterations)
        print(player2Win / iterations)
        if(player1Win > player2Win):
            return 1
        return 2

if __name__ == "__main__":
    b1 = Bot()
    b2 = Bot()
    game = Game(b1,b2, debug=True)
    # better_bot = game.train()
    # if(better_bot == 1) game.player2 = b1
    # else game.player2 = b2
    # game.player1 = Player()
    # game.debug = True
    # game = Game(debug=True)
    game.play()        
