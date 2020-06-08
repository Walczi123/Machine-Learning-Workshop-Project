class Player:
    def __init__(self):
        pass

    def move(self):
        x, y = input("Input x and y:  ").split() 
        return (int(x), int(y))

class Bot(Player):
    def __init__(self):
        pass

    def move(self):
        # state = self.states[-1]
        # nextStates = []
        # nextPositions = []
        # for i in range(BOARD_ROWS):
        #     for j in range(BOARD_COLS):
        #         if state.data[i, j] == 0:
        #             nextPositions.append([i, j])
        #             nextStates.append(state.nextState(i, j, self.symbol).getHash())
        # if np.random.binomial(1, self.exploreRate):
        #     np.random.shuffle(nextPositions)
        #     # Not sure if truncating is the best way to deal with exploratory step
        #     # Maybe it's better to only skip this step rather than forget all the history
        #     self.states = []
        #     action = nextPositions[0]
        #     action.append(self.symbol)
        #     return action

        # values = []
        # for hash, pos in zip(nextStates, nextPositions):
        #     values.append((self.estimations[hash], pos))
        # np.random.shuffle(values)
        # values.sort(key=lambda x: x[0], reverse=True)
        # action = values[0][1]
        # action.append(self.symbol)
        # return action
        return (1, 1)
    