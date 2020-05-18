class Player:
    def __init__(self):
        pass

    def move(self):
        x, y = input("Input x and y:  ").split() 
        return (int(x), int(y))
    