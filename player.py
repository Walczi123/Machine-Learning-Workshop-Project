import numpy as np

class Player:
    def __init__(self):
        pass

    def move(self):
        x, y = input("Input x and y:  ").split() 
        return (int(x), int(y))

class Bot(Player):
    def __init__(self, exploreRate = 0.3):
        self.exploreRate = exploreRate
        self.states = []
        self.estimations = dict()
        pass

    def move(self):

        state = self.states[-1]
        nextStates = []
        nextPositions = []
        for i in range(-100, 100):
            for j in range(-100, 100):
                if (i,j) not in self.states:
                    nextPositions.append([i,j])
                    nextStates.append(state.nextState(i,j).getHash())

        if np.random.binomial(1, self.exploreRate):
            np.random.shuffle(nextPositions)
            self.states=[]
            action=nextPositions[0]
            return action

        values = []
        for hash, pos in zip(nextStates, nextPositions):
            values.append((self.estimations[hash], pos))
        np.random.shuffle(values)
        values.sort(key=lambda x: x[0], reverse=True)
        action = values[0][1]
        return action
    