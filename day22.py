from enum import Enum

class Stage(Enum):
    Clear = 0
    Weakened = 1
    Infected = 2
    Flagged = 3

class Direction(Enum):
    North = (-1,0)
    East = (0,1)
    South = (1,0)
    West = (0,-1)

class Turn(Enum):
    Left = 0
    Right = 1

def readInput(filename):
    grid = []
    with open(filename, 'r') as file:
        for eachLine in file:
            gridLine = []
            for eachC in eachLine.strip():
                if eachC == '#':
                    gridLine.append(Stage.Infected.value)
                else:
                    gridLine.append(Stage.Clear.value)
            grid.append(gridLine)
    return grid

def expandGrid(grid, pos):
    oSize = len(grid)
    expGrid = [[Stage.Clear.value for j in range(oSize*3)]for i in range(oSize*3)]
    for i in range(oSize):
        for j in range(oSize):
            expGrid[oSize+i][oSize+j] = grid[i][j]
    return (expGrid, (pos[0]+oSize, pos[1]+oSize, pos[2]))

def onBoundary(pos, gridSize):
    return pos[0] == 0 or pos[0] == gridSize-1 or pos[1] == 0 or pos[1] == gridSize-1

def reverse(pos):
    dir = pos[2]
    if dir == Direction.North:
        return Direction.South
    elif dir == Direction.East:
        return Direction.West
    elif dir == Direction.South:
        return Direction.North
    else:
        return Direction.East

def makeTurn(pos, turn):
    dir = pos[2]
    if dir == Direction.North:
        if turn == Turn.Left:
            dir = Direction.West
        else:
            dir = Direction.East
    elif dir == Direction.East:
        if turn == Turn.Left:
            dir = Direction.North
        else:
            dir = Direction.South
    elif dir == Direction.South:
        if turn == Turn.Left:
            dir = Direction.East
        else:
            dir = Direction.West
    else:
        if turn == Turn.Left:
            dir = Direction.South
        else:
            dir = Direction.North
    return dir

def step(pos, dir):
    return [pos[0]+dir.value[0], pos[1]+dir.value[1], dir]

def burst(pos, grid, infectionBurst):
    row = pos[0]
    col = pos[1]

    if grid[row][col] == Stage.Infected.value:
        newDir = makeTurn(pos, Turn.Right)
        grid[row][col] = Stage.Clear.value
        return step(pos, newDir)
    else:
        newDir = makeTurn(pos, Turn.Left)
        grid[row][col] = Stage.Infected.value
        infectionBurst[0] += 1
        return step(pos, newDir)

def newBurst(pos, grid, infectionBurst):
    row = pos[0]
    col = pos[1]

    if grid[row][col] == Stage.Clear.value:
        newDir = makeTurn(pos, Turn.Left)
    elif grid[row][col] == Stage.Weakened.value:
        newDir = pos[2]
        infectionBurst[0] += 1
    elif grid[row][col] == Stage.Infected.value:
        newDir = makeTurn(pos, Turn.Right)
    else:
        newDir = reverse(pos)
    grid[row][col] = (1+grid[row][col]) % 4
    return step(pos, newDir)

def totalInfected(grid):
    rowSum =[]
    for i in range(len(grid)):
        rowSum.append(sum(grid[i]))
    return sum(rowSum)

def Solution1(filename, n):
    infectionBurst = {0:0}
    grid = readInput(filename)
    currentPos = [int(len(grid)/2), int(len(grid)/2), Direction.North]
    print(totalInfected(grid))
    for i in range(n):
        currentPos = burst(currentPos, grid, infectionBurst)
        if onBoundary(currentPos, len(grid)):
            expansion = expandGrid(grid, currentPos)
            grid = expansion[0]
            currentPos = expansion[1]
            print(totalInfected(grid))
    print(totalInfected(grid))
    return infectionBurst[0]

def Solution2(filename, n):
    infectionBurst = {0:0}
    grid = readInput(filename)
    currentPos = [int(len(grid)/2), int(len(grid)/2), Direction.North]
    for i in range(n):
        currentPos = newBurst(currentPos, grid, infectionBurst)
        if onBoundary(currentPos, len(grid)):
            expansion = expandGrid(grid, currentPos)
            grid = expansion[0]
            currentPos = expansion[1]
    return infectionBurst[0]



#print(Solution1('day22Input.txt', 10000))
print(Solution2('day22Input.txt', 10000000))






