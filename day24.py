def readInput(filename):
    positions = []
    with open(filename, 'r') as file:
        for eachLine in file:
            splitted = eachLine.strip().split('/')
            positions.append([int(splitted[0]), int(splitted[1])])
    return positions

def findPaths(contextPath, target, positions):
    allPaths = []
    extendPath = False
    for i in range(len(positions)):
        if positions[i][0] == target or positions[i][1] == target:
            extendPath = True
            newTarget = positions[i][1] if positions[i][0] == target else positions[i][0]
            allPaths += findPaths(contextPath+[positions[i]], newTarget, positions[:i]+positions[i+1:])
    if not extendPath:
        allPaths.append(contextPath)
    return allPaths

def allPaths(allPos):
    allPaths = []
    for i in range(len(allPos)):
        if allPos[i][0] == 0:
            paths = findPaths([allPos[i]], allPos[i][1], allPos[:i]+allPos[i+1:])
            for eachPath in paths:
                allPaths.append(eachPath)
    return allPaths

def maxPath(paths):
    allPathV = []
    for eachPath in paths:
        pathV = 0
        for eachElem in eachPath:
            pathV += eachElem[0]
            pathV += eachElem[1]
        allPathV.append(pathV)
    return max(allPathV)

def longestPaths(paths):
    longest = 0
    longestPaths = []
    for eachPath in paths:
        if len(eachPath) > longest:
            longestPaths = [eachPath]
            longest = len(eachPath)
        elif len(eachPath) == longest:
            longestPaths.append(eachPath)
    return longestPaths



#allPos=[[0,2],[2,2],[2,3],[3,4],[3,5],[0,1],[10,1],[9,10]]
#print(maxPath(longestPaths(allPaths(allPos))))


def Solution1():
    allPos = readInput('day24Input.txt')
    print(maxPath(allPaths(allPos)))

def Solution2():
    allPos = readInput('day24Input.txt')
    print(maxPath(longestPaths(allPaths(allPos))))

Solution2()
