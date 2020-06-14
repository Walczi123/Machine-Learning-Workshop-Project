from player import Player, Bot
from game import Game

#p1 = Player()
p2 = Player()
#p2 = Bot(2)
#p2.loadPolicy()
p1 = Bot(1)
p1.loadPolicy()
game = Game(p1, p2, need_for_win=3, boardSize = 5)
game.debug = True
ans = ""
while(ans != "n"):
    game.play() 
    ans = ""
    while ans != "n" and ans !="y" :
        if ans != "":
            print("Please, type correct anwser")
        ans = input("Would you like to play again? y/n  ")
    print("Thank you for playing")
    