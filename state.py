import numpy as np
import math
class State:
    def __init__(self):
        self.data = []
        self.winner = None
        self.end = False

    def addMove(self,move):
        if findCell(self.data,move[0],move[1]):
            print("This cell is already occupied! Try again")
            return False
        self.data.append(move)
        return True

    def isEnd(self):
        if self.end is not False:
            return self.end      
        for i in range(0, len(self.data), 2):
            x,y = self.data[i]
            for j in range(i+2, len(self.data), 2):
                x2,y2 = self.data[j]
                if (x == x2 + 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 - 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 and (y == y2-1 or y == y2+1)):
                    xdiff = x-x2
                    ydiff = y-y2
                    for k in range(j+2, len(self.data), 2):
                        x3,y3 = self.data[k]
                        if np.abs(xdiff) == 1 and ydiff == 0:
                            if y == y3 and (x == x3 - xdiff or x2 == x3 + xdiff):
                                self.winner = 1
                                self.end = True
                                return self.end
                        elif xdiff == 0 and np.abs(ydiff) == 1:
                            if x == x3 and (y == y3 - ydiff or y2 == y3 + ydiff):
                                self.winner = 1
                                self.end = True
                                return self.end
                        else:
                            if (x == x3 - xdiff and y == y3 - ydiff) or (x2 == x3 + xdiff and y2 == y3 + ydiff):
                                self.winner = 1
                                self.end = True
                                return self.end
        for i in range(1, len(self.data), 2):
            x,y = self.data[i]
            for j in range(i+2, len(self.data), 2):
                x2,y2 = self.data[j]
                if (x == x2 + 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 - 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 and (y == y2-1 or y == y2+1)):
                    xdiff = x-x2
                    ydiff = y-y2
                    for k in range(j+2, len(self.data), 2):
                        x3,y3 = self.data[k]
                        if np.abs(xdiff) == 1 and ydiff == 0:
                            if y == y3 and (x == x3 - xdiff or x2 == x3 + xdiff):
                                self.winner = 2
                                self.end = True
                                return self.end
                        elif xdiff == 0 and np.abs(ydiff) == 1:
                            if x == x3 and (y == y3 - ydiff or y2 == y3 + ydiff):
                                self.winner = 2
                                self.end = True
                                return self.end
                        else:
                            if (x == x3 - xdiff and y == y3 - ydiff) or (x2 == x3 + xdiff and y2 == y3 + ydiff):
                                self.winner = 2
                                self.end = True
                                return self.end
        self.end = False
        return self.end
    
    def martinIsEnd(self):
        win=3
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
        print("",end="   ")
        for y in range(minwidth,maxwidth+1):
            print(y,end="   ")
        for y in range(maxheight,minheight-1,-1):
            print("\n")
            print(y,end="   ")
            for x in range(minwidth,maxwidth+1):
                cell=findCell(list,x,y)
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
