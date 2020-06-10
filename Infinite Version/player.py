import numpy as np
from state import findCell
import pickle
import os.path
import random

class Player:
    def __init__(self):
        pass

    def move(self, state):
        while(True):
            anw = input("Input x and y:  ").split()
            try:
                return (int(anw[0]), int(anw[1]))
            except ValueError:
                print("Incorrect values")

# AI Player
class Bot(Player):
    def __init__(self, id, limiter = 5,stepSize=0.1, exploreRate = 0.3):
        self.exploreRate = exploreRate
        self.states = []
        self.stepSize = stepSize
        self.estimations = dict()
        self.limiter = limiter
        self.bounds = limiter
        self.stepSize = stepSize
        self.id = id
        pass
    
    # decision making
    def move(self, state):
        nextStates = []
        nextPositions = []
        for i in range(-self.limiter, self.limiter+1):
            for j in range(-self.limiter, self.limiter+1):
                if (i,j) not in state.data:
                    nextPositions.append((i,j))
                    nextStates.append(state.nextState(i,j).getHash())
                    if state.nextState(i,j).getHash() not in self.estimations:
                        if state.nextState(i,j).isEnd:
                            if state.nextState(i,j).winner == id:
                                self.estimations[state.nextState(i,j).getHash()] = 1
                            else:
                                self.estimations[state.nextState(i,j).getHash()] = 0
                        else : 
                            self.estimations[state.nextState(i,j).getHash()] = 0.5
        
        if len(nextPositions) == 0:
            self.limiter += self.bounds
            return self.move(state)

        if np.random.binomial(1, self.exploreRate):
            r = random.randint(0, len(nextPositions)-1)
            action=nextPositions[r]
            self.states.append(nextStates[r])
            return action

        values = []
        for hash, pos in zip(nextStates, nextPositions):
            values.append((self.estimations[hash], pos))
        v = values.index(max(values, key=lambda item:item[0]))
        action = values[v][1]
        self.states.append(nextStates[v])
        return action
    
    # update estimation according to reward
    def feedReward(self, reward):
        if len(self.states) == 0:
            return
        target = reward
        for latestState in reversed(self.states):
            value = self.estimations[latestState] + self.stepSize * (target - self.estimations[latestState])
            self.estimations[latestState] = value
            target = value
        self.states = []

    # save learing data
    def savePolicy(self):
        fw = open('optimal_policy_' + str(self.id), 'wb')
        pickle.dump(self.estimations, fw)
        fw.close()

    # save learing data
    def loadPolicy(self):
        if not os.path.exists('optimal_policy_' + str(self.id)):
            return
        fr = open('optimal_policy_' + str(self.id),'rb')
        self.estimations = pickle.load(fr)
        fr.close()
    