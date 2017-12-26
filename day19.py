from copy import copy
from enum import Enum

class Motion(Enum):
    VERTICAL = 1
    HORIZONTAL = 2

def getMap(filename):
    mymap = []
    with open(filename, 'r') as file:
        for eachLine in file:
            mymap.append(eachLine)
    return mymap

def getStarting(mymap):
    for i in range(len(mymap[0])):
        if mymap[0][i] == '|':
            return (0,i)
    return (0,-1)

def moveDown(start, mymap, width, collected):
    for r in range(start[0], len(mymap)):
        if mymap[r][start[1]] == ' ':
            return r - start[0]
        if mymap[r][start[1]] == '+':
            break
        if mymap[r][start[1]].isalpha():
            collected.append(mymap[r][start[1]])
    turned = makeTurn((r, start[1]), mymap, width, Motion.VERTICAL)
    if turned[1] > start[1]:
        return r-start[0]+1+moveRight(turned, mymap, width, collected)
    else:
        return r-start[0]+1+moveLeft(turned, mymap, width, collected)

def moveUp(start, mymap, width, collected):
    for r in range(start[0], 0, -1):
        if mymap[r][start[1]] == ' ':
            return start[0] - r
        if mymap[r][start[1]] == '+':
            break
        if mymap[r][start[1]].isalpha():
            collected.append(mymap[r][start[1]])
    turned = makeTurn((r, start[1]), mymap, width, Motion.VERTICAL)
    if turned[1] > start[1]:
        return start[0]-r+1+moveRight(turned, mymap, width, collected)
    else:
        return start[0]-r+1+moveLeft(turned, mymap, width, collected)

def moveLeft(start, mymap, width, collected):
    for c in range(start[1], -1, -1):
        if mymap[start[0]][c] == ' ':
            return start[1] - c
        if mymap[start[0]][c] == '+':
            break
        if mymap[start[0]][c].isalpha():
            collected.append(mymap[start[0]][c])
    turned = makeTurn((start[0], c), mymap, width, Motion.HORIZONTAL)
    if turned[0] > start[0]:
        return start[1]-c+1+moveDown(turned, mymap, width, collected)
    else:
        return start[1]-c+1+moveUp(turned, mymap, width, collected)

def moveRight(start, mymap, width, collected):
    for c in range(start[1], width):
        if mymap[start[0]][c] == ' ':
            return c - start[1]
        if mymap[start[0]][c] == '+':
            break
        if mymap[start[0]][c].isalpha():
            collected.append(mymap[start[0]][c])
    turned = makeTurn((start[0], c), mymap, width, Motion.HORIZONTAL)
    if turned[0] > start[0]:
        return c-start[1]+1+moveDown(turned, mymap, width, collected)
    else:
        return c-start[1]+1+moveUp(turned, mymap, width, collected)

def makeTurn(cross, mymap, width, mymotion):
    x = cross[0]
    y = cross[1]
    if mymotion == Motion.VERTICAL:
        if y != 0 and mymap[x][y-1] == '-':
            return (x, y-1)
        elif y != width and mymap[x][y+1] == '-':
            return (x, y+1)
        else:
            raise ValueError()
    else:
        if x != 0 and mymap[x-1][y] == '|':
            return (x-1, y)
        elif x != len(mymap) and mymap[x+1][y] == '|':
            return (x+1, y)
        else:
            raise ValueError()

def navigate():
    mymap = getMap('day19Input.txt')
    start = getStarting(mymap)
    width = max([len(mymap[i]) for i in range(len(mymap))])
    fixedMap = [mymap[i].ljust(width) for i in range(len(mymap))]
    letters = []
    traveled = moveDown(start, fixedMap, width, letters)
    return (traveled, ''.join(letters))

def Solution():
    print(navigate())

Solution()


