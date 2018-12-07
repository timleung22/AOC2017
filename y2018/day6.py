maxDistance = 32
def manhattanDist(pointA, pointB):
    return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1])

def findEdges(coordinates):
    xCoordinates = []
    yCoordinates = []
    for eachC in coordinates:
        xCoordinates.append(eachC[0])
        yCoordinates.append(eachC[1])
    return (min(xCoordinates), min(yCoordinates), max(xCoordinates), max(yCoordinates))

def readCoordinates():
    coordinates = []
    with open("day6Sample.txt", "r") as f:
        for eachLine in f:
            comma = eachLine.index(",")
            xCoor = eachLine[:comma]
            yCoor = eachLine[comma+2:-1]
            coordinates.append([int(xCoor), int(yCoor)])
    return coordinates

def isEdge(coord, edges):
    return coord[0] == edges[0] or coord[1] == edges[1] or coord[0] == edges[2] or coord[1] == edges[3]

def getScores(coordinates, edges):
    scores = []
    for i in range(len(coordinates)):
        scores.append(0)

    for y in range(edges[1], edges[3]+1):
        for x in range(edges[0], edges[2]+1):
            distances = []
            for eachC in coordinates:
                distances.append(manhattanDist([x,y], eachC))
            minDistance = min(distances)
            if distances.count(minDistance) == 1:
                scores[distances.index(minDistance)] += 1
    return scores

def calTotalManhattanDistances(coordinates, coord):
    accDistance = 0
    for eachC in coordinates:
        accDistance += manhattanDist(eachC, coord)
    return accDistance

def buildGridWithSafeArea(coordinates, edges):
    grid = [[0 for x in range(edges[2]+1-edges[0])] for y in range(edges[3]+1-edges[1])]
    for y in range(edges[1], edges[3]+1):
        for x in range(edges[0], edges[2]+1):
            distancesSum = calTotalManhattanDistances(coordinates, [x, y])
            if distancesSum < maxDistance:
                grid[y-edges[1]][x-edges[0]] = 1
    return grid

def isSafe(grid, row, col, visited):
    print([row, col])
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1 and not visited[row][col]

rowNbor = [-1, -1, -1, 0, 0, 1, 1, 1]
colNbor = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(grid, visited, row, col, counted):
    visited[row][col] = True
    for i in range(len(rowNbor)):
        y = row + rowNbor[i]
        x = col + colNbor[i]
        if isSafe(grid, y, x, visited):
            counted += 1
            counted = dfs(grid, visited, y, x, counted)
    return counted

def largesRegion(grid):
    visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    largestArea = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1 and not visited[y][x]:
                count = 1
                count += dfs(grid, visited, y, x, count)
                largestArea = max([largestArea, count])

    return largestArea

def Solution1():
    coordinates = readCoordinates()
    edges = findEdges(coordinates)

    scores1 = getScores(coordinates, edges)
    scores2 = getScores(coordinates, [0, 0, edges[2]+10, edges[3]+10])

    commonScores = []
    for i, s in enumerate(scores1):
        if isEdge(coordinates[i], edges):
            commonScores.append(-1)
        elif s == scores2[i]:
            commonScores.append(s)
        else:
            commonScores.append(-1)

    print(commonScores)
    print(max(commonScores))

def Solution2():
    coordinates = readCoordinates()
    edges = findEdges(coordinates)
    grid = buildGridWithSafeArea(coordinates, edges)
    for eachRow in grid:
        print(eachRow)
    print(largesRegion(grid))


Solution2()



