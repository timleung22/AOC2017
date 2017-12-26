from functools import reduce
from math import sqrt

def rotateCounterClockwise(grid):
    return list(reversed(list(zip(*grid))))

def rotateClockwise(grid):
    return list(zip(*grid[::-1]))

def flipLR(grid):
    flipped = []
    for eachLine in grid:
        flipped.append(list(reversed(eachLine)))
    return flipped

def flipTB(grid):
    return list(reversed(grid))

def gridToLine(grid):
    output = ''
    for eachRow in grid:
        line = ''
        for eachC in eachRow:
            if eachC == 0:
                line += '.'
            else:
                line += '#'
        output += line
        output += '/'
    return output[:-1]

def lineToGrid(line):
    grid = []
    for part in line.strip().split('/'):
        row = []
        for eachC in part:
            if eachC == '.':
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid

def readRules():
    rules = {}
    transformSign = ' => '
    with open('day21Input.txt', 'r') as file:
        for eachLine in file:
            idx = eachLine.index(transformSign)
            ruleFrom = eachLine[0:idx].strip()
            ruleTo = eachLine[idx+len(transformSign):].strip()
            rules[ruleFrom] = ruleTo
    return rules

def transform(grid, rules):
    line = gridToLine(grid)
    transformTarget = rules.get(line)
    if transformTarget == None:
        return None
    else:
        return lineToGrid(transformTarget)

def rotateAndFlipAndTransform(grid, rules):
    rotation = 0
    rotated = grid
    while rotation < 3:
        rotated = rotateClockwise(rotated)
        rotation += 1
        transformed = transform(rotated, rules)
        if transformed != None:
            return transformed
        else:
            flippedTransformed = flipAndTransform(rotated, rules)
            if flippedTransformed != None:
                return flippedTransformed
    return None

def flipAndTransform(grid, rules):
    flippedTB = flipTB(grid)
    transformed = transform(flippedTB, rules)
    if transformed != None:
        return transformed
    flippedLR = flipLR(grid)
    return transform(flippedLR, rules)

def countOnBits(grid):
    count = 0
    for eachLine in grid:
        count += reduce((lambda x,y: x+y), eachLine)
    return count

def splitGrid(grid):
    if len(grid) % 2 == 0:
        return splitTo2By2(grid)
    else:
        return splitTo3By3(grid)

def splitTo2By2(grid):
    splitted = []
    splitCount = int(len(grid) / 2)
    for i in range(splitCount):
        for j in range(splitCount):
            rowBegin = i*2
            columnBegin = j*2
            smaller = [grid[rowBegin][columnBegin:columnBegin+2], grid[rowBegin+1][columnBegin:columnBegin+2]]
            splitted.append(smaller)
    return splitted

def splitTo3By3(grid):
    splitted = []
    splitCount = int(len(grid) / 3)
    for i in range(splitCount):
        for j in range(splitCount):
            rowBegin = i*3
            columnBegin = j*3
            smaller = []
            for k in range(3):
                smaller.append(grid[rowBegin+k][columnBegin:columnBegin+3])
            splitted.append(smaller)
    return splitted

def mergeGrid(splitted):
    dimension = int(sqrt(len(splitted)))
    splittedGridDimension = len(splitted[0])
    merged = []
    for k in range(dimension):
        for j in range(splittedGridDimension):
            line = []
            for i in range(dimension):
                line += splitted[k*dimension+i][j]
            merged.append(line)
    return merged



def Solution1():
    grid = [[0,1,0],[0,0,1],[1,1,1]]
    transformRules = readRules()
    for iteration in range(18):
        toMerge = []
        for eachSplitted in splitGrid(grid):
            transformed =  transform(eachSplitted, transformRules)
            if transformed != None:
                toMerge.append(transformed)
            else:
                transformed = flipAndTransform(eachSplitted, transformRules)
                if transformed != None:
                    toMerge.append(transformed)
                else:
                    transformed = rotateAndFlipAndTransform(eachSplitted, transformRules)
                    if transformed != None:
                        toMerge.append(transformed)
                    else:
                        raise AssertionError('No Transformation result')
        grid = mergeGrid(toMerge)
    return countOnBits(grid)

def splitMergeTest(grid):
    print(grid)
    x = splitGrid(grid)
    print(x)
    y = mergeGrid(x)
    print(y)

#splitMergeTest([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#splitMergeTest([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]])
#splitMergeTest([[i*9+j for j in range(9)] for i in range(9)])


print(Solution1())





