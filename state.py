import numpy as np
import math

class State:
    def __init__(self, need_for_win):
        self.data = []
        self.winner = None
        self.end = False
        self.need_for_win = need_for_win

    def addMove(self,move):
        if findCell(self.data,move[0],move[1]):
            print("This cell is already occupied! Try again")
            return False
        self.data.append(move)
        return True
    
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
                
    def printVector(self):
        vector = self.data
        # list = []
        # for index in range(len(self.data)):
        #     if (index%2)==0:
        #         label="X"
        #     else:
        #         label="O"
        #     list.append((vector[index][0],vector[index][1],label))
        maxwidth=max(vector,key=lambda x:x[0])[0]
        minwidth=min(vector,key=lambda x:x[0])[0]
        maxheight=max(vector,key=lambda x:x[1])[1]
        minheight=min(vector,key=lambda x:x[1])[1]    
        print("",end="   ")
        for y in range(minwidth,maxwidth+1):
            print(y,end="   ")
        for y in range(maxheight,minheight-1,-1):
            print("\n")
            print(y,end="   ")
            for x in range(minwidth,maxwidth+1):
                cell=findCell(vector,x,y)
                if(cell):
                    print(cell[0][2],end="   ")
                else:
                    print(".",end="   ")
        print("\n")

def findCell(vector,x,y):
    result=[item for item in vector if item[0]==x and item[1]==y]
    return result

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
    for shift in range(maxWin,minWin-1,-1):
        if [item for item in playerList if item[0]==(cell[0]+shift) and item[1]==(cell[1]+shift)]:
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

    def getHash(self):
        return hash(frozenset(self.data))
