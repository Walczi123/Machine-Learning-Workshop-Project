def print2(vector):
    list=[]
    for index in range(len(vector)):
        if (index%2)==0:
            label="X"
        else:
            label="O"
        list.append((vector[index][0],vector[index][1],label))
    list=sorted(list,key=lambda x: (x[0],x[1]))
    print(list)
    width=max(list,key=lambda x:x[0])[0]-min(list,key=lambda x:x[0])[0]
    height=max(list,key=lambda x:x[1])[1]-min(list,key=lambda x:x[1])[1]
    print(width)
    print(height)
    for y in range(height+1):
        print("\n")
        for x in range(width+1):
            cell=findCell(list,x,y)
            if(cell):
                print(cell[0][2],end=" ")
            else:
                print("*",end=" ")

def findCell(vector,x,y):
    result=[item for item in vector if item[0]==x and item[1]==y]
    return result


vec=[(1,2),(3,4),(0,0),(5,3)]
print2(vec)

