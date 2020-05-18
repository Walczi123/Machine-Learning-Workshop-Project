class State:
    def __init__(self):
        self.data = []
        self.winner = None
        self.end = False

    def addMove(self,move):
        self.data.append(move)    

    def isEnd(self):
        pass

