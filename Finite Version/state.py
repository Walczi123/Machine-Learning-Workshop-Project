import numpy as np
import math

# class with board informations
class State:
    def __init__(self, need_for_win, boardSize):
        self.data = []
        self.winner = None
        self.end = False
        self.need_for_win = need_for_win
        self.boardSize = boardSize

    # if move is correct add to list
    def addMove(self,move):
        if findCell(self.data,move[0],move[1]):
            print("This cell is already occupied! Try again")
            return False
        if abs(move[0]) > math.ceil(self.boardSize/2) - 1 or abs(move[1]) > math.ceil(self.boardSize/2) - 1:
            print("This cell is outside of bounds! Try again")
            return False
        self.data.append(move)
        return True
    
    # end condition
    def isEnd(self):
        win=self.need_for_win
        minWin=math.floor((win-1)/2)
        maxWin=math.ceil(win/2)
        if self.end is True:
            return self.end
        listPlayer1=self.data[0::2]
        listPlayer2=self.data[1::2]
        for elem in listPlayer1:
            if checkCell(elem,listPlayer1,win,minWin,maxWin) == True:
                self.end=True
                self.winner=1
                return self.end
        for elem in listPlayer2:
            if checkCell(elem,listPlayer2,win,minWin,maxWin) == True:
                self.end=True
                self.winner=2
                return self.end
        if len(self.data) == self.boardSize * self.boardSize:
                self.end=True
                self.winner=0
                return self.end
     

    # print board    
    def printVector(self):
        vector = self.data
        list = []
        for index in range(len(self.data)):
            if (index%2)==0:
                label="X"
            else:
                label="O"
            list.append((vector[index][0],vector[index][1],label))
        maxwidth=max(list,key=lambda x:x[0])[0]
        minwidth=min(list,key=lambda x:x[0])[0]
        maxheight=max(list,key=lambda x:x[1])[1]
        minheight=min(list,key=lambda x:x[1])[1]    
        print(" ",end="   ")
        for y in range(minwidth,maxwidth+1):
            if y < 0:
                print(y,end="  ")
            else:
                print(" " + str(y),end="  ")
        for y in range(maxheight,minheight-1,-1):
            print("\n")
            if y >= 0:
                print(" " + str(y), end="   ")
            else:
                print(y,end="   ")
            for x in range(minwidth,maxwidth+1):
                cell=findCell(list,x,y)
                if(cell):
                    print(cell[0][2],end="   ")
                else:
                    print(".",end="   ")
        print("\n")
    
    # create the hash of states
    def getHash(self):
        return hash(frozenset(self.data))

    # create all posible next moves
    def nextState(self, i, j):
        newState = State(self.need_for_win, self.boardSize)
        newState.data = self.data.copy()
        newState.data.append((i, j))
        return newState

# find cell if exists
def findCell(vector,x,y):
    result = None
    result=[item for item in vector if item[0]==x and item[1]==y]
    return result

# get symbol of the cell
def checkCell(cell,playerList,win,minWin,maxWin):
    count=0
    for shift in range(-minWin,maxWin+1):
        if [item for item in playerList if item[0]==(cell[0]+shift) and item[1]==(cell[1]+shift)]:
            count=count+1
            if count == win:
                return True
        else:
            break
    count=0
    for shift in range(-minWin,maxWin+1):
        if [item for item in playerList if item[0]==(cell[0]-shift) and item[1]==(cell[1]+shift)]:
            count=count+1
            if count == win:
                return True
        else:
            break
    count=0
    for shift in range(-minWin,maxWin+1):
        if [item for item in playerList if item[0]==(cell[0]+shift) and item[1]==cell[1]]:
            count=count+1
            if count == win:
                return True
        else:
            break
    count=0
    for shift in range(-minWin,maxWin+1):
        if [item for item in playerList if item[0]==cell[0] and item[1]==(cell[1]+shift)]:
            count=count+1
            if count == win:
                return True
        else:
            break
    return False
