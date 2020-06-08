import numpy as np
from state import findCell
import pickle

class Player:
    def __init__(self):
        pass

    def move(self, state):
        x, y = input("Input x and y:  ").split() 
        return (int(x), int(y))

class Bot(Player):
    def __init__(self, limiter = 5,stepSize=0.1, name = 'bot', exploreRate = 0.3):
        self.exploreRate = exploreRate
        self.states = []
        self.stepSize = stepSize
        self.name = name
        self.estimations = dict()
        self.limiter = limiter
        pass

    def move(self, state):
        #state = self.states[-1]

        nextStates = []
        nextPositions = []
        for i in range(-self.limiter, self.limiter):
            for j in range(-self.limiter, self.limiter):
                if findCell(state.data, i, j) != None:
                    nextPositions.append((i,j))
                    nextStates.append(state.nextState(i,j).getHash())

        #if np.random.binomial(1, self.exploreRate):
            np.random.shuffle(nextPositions)
            self.states=[]
            action=nextPositions[0]
            return action

        #values = []
        #for hash, pos in zip(nextStates, nextPositions):
        #    values.append((self.estimations[hash], pos))
        #np.random.shuffle(values)
        #values.sort(key=lambda x: x[0], reverse=True)
        #action = values[0][1]
        #return action
    
    # update estimation according to reward
    def feedReward(self, reward):
        if len(self.states) == 0:
            return
        self.states = [state.getHash() for state in self.states]
        target = reward
        for latestState in reversed(self.states):
            value = self.estimations[latestState] + self.stepSize * (target - self.estimations[latestState])
            self.estimations[latestState] = value
            target = value
        self.states = []

    def savePolicy(self):
        fw = open('optimal_policy_' + self.name, 'wb')
        pickle.dump(self.estimations, fw)
        fw.close()

    def loadPolicy(self):
        fr = open('optimal_policy_' + self.name,'rb')
        self.estimations = pickle.load(fr)
        fr.close()
    