import utils

def squareSize(input):
    i = 1
    while i*i < input:
        i += 2

    return i

def Solution1(input):
    size = squareSize(input)
    port = ((size-1)/2, (size-1)/2)
    stepsFromInnerLoopEnd = input - (size-2)*(size-2)
    endOfInnerLoop = (size-2, size-2)
    inputCoord = findCoordForInput(endOfInnerLoop, stepsFromInnerLoopEnd, (size-1, size-1))
    return utils.mdist(port, inputCoord)

def findCoordForInput(lastCoord, steps, maxCoord):
    if steps == 1:
        return (lastCoord[0], lastCoord[1]+1)
    else:
        remainingSteps = steps-1
        nextRowIdx = lastCoord[0]
        nextColIdx = lastCoord[1]+1
        while remainingSteps > 0 and nextRowIdx > 0:
            nextRowIdx -= 1
            remainingSteps -= 1
        while remainingSteps > 0 and nextColIdx > 0:
            nextColIdx -= 1
            remainingSteps -= 1
        while remainingSteps > 0 and nextRowIdx < maxCoord[0]:
            nextRowIdx += 1
            remainingSteps -= 1
        while remainingSteps > 0 and nextColIdx < maxCoord[0]:
            nextColIdx += 1
            remainingSteps -= 1

        return (nextRowIdx, nextColIdx)

def buildGrid(size, lastGrid, limit):
    if size == 1:
        return ([[1]], 1)
    else:
        grid = [[0 for col in range(size)] for row in range(size)]
        grid = copyFromLastGrid(grid, lastGrid, size)
        return addBorder(grid, size, limit)

def copyFromLastGrid(grid, lastGrid, size):
    for row in range(1, size-1):
        for col in range(1, size-1):
            grid[row][col] = lastGrid[row-1][col-1]

    return grid

def addBorder(grid, size, limit):
    row, col = size-2, size-1
    grid[row][col] = sumOfNeighbors(grid, row, col, size)
    if (grid[row][col] > limit):
        return (grid, grid[row][col])
    row -= 1
    while row > 0:
        grid[row][col] = sumOfNeighbors(grid, row, col, size)
        if (grid[row][col] > limit):
            return (grid, grid[row][col])
        row -= 1
    while col > 0:
        grid[row][col] = sumOfNeighbors(grid, row, col, size)
        if (grid[row][col] > limit):
            return (grid, grid[row][col])
        col -= 1
    while row < size - 1:
        grid[row][col] = sumOfNeighbors(grid, row, col, size)
        if (grid[row][col] > limit):
            return (grid, grid[row][col])
        row += 1
    while col < size:
        grid[row][col] = sumOfNeighbors(grid, row, col, size)
        if (grid[row][col] > limit):
            return (grid, grid[row][col])
        col += 1

    return (grid, grid[size-1][size-1])

def sumOfNeighbors(grid, row, col, size):
    sum = 0
    if row != 0:
        sum += grid[row-1][col]
        if col != 0:
            sum += grid[row-1][col-1]
        if col != size-1:
            sum += grid[row-1][col+1]
    if col != 0:
        sum += grid[row][col-1]
    if col != size-1:
        sum += grid[row][col+1]
    if row != size-1:
        sum += grid[row+1][col]
        if col != 0:
            sum += grid[row+1][col-1]
        if col != size-1:
            sum += grid[row+1][col+1]

    return sum

def buildSolution(limit):
    lastGrid = [[]]
    size = 1
    while True:
        (lastGrid, max) = buildGrid(size, lastGrid, limit)
        size += 2
        if max > limit:
            return max

print(buildSolution(289326))

#print(findCoordForInput((3,3), 11, (4,4)))
#print(Solution1(289326))

