import re

def initFabric():
    fabric = [[]]
    for y in range(1000):
        fabric.append([])
        for x in range(1000):
            fabric[y].append(0)
    return fabric

def addClaim(fabric, claim):
    match = re.search(r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)\n', claim)
    id = int(match.group(1))
    fromLeft = int(match.group(2))
    fromTop = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))

    for y in range(fromTop, fromTop+height):
        for x in range(fromLeft, fromLeft+width):
            if fabric[y][x] == 0:
                fabric[y][x] = id
            else:
                fabric[y][x] = -1
    return fabric

def findIndependent(fabric, claim):
    match = re.search(r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)\n', claim)
    id = int(match.group(1))
    fromLeft = int(match.group(2))
    fromTop = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))

    noOverlap = True
    for y in range(fromTop, fromTop+height):
        for x in range(fromLeft, fromLeft+width):
            noOverlap = noOverlap and (fabric[y][x] == id)
    return noOverlap


def countOverlaps(fabric):
    count = 0
    for y in range(1000):
        for x in range(1000):
            if fabric[y][x] == -1:
                count += 1
    return count

def Solution1(input):

    fabric = initFabric()
    inputLines = []
    with open(input, "r") as f:
        for eachLine in f:
            inputLines.append(eachLine)

    for eachInput in inputLines:
        fabric = addClaim(fabric, eachInput)

    print(countOverlaps(fabric))


def Solution2(input):
    fabric = initFabric()
    inputLines = []
    with open(input, "r") as f:
        for eachLine in f:
            inputLines.append(eachLine)

    for eachInput in inputLines:
        fabric = addClaim(fabric, eachInput)
    for eachInput in inputLines:
        if (findIndependent(fabric, eachInput)):
            print(eachInput)

Solution2("day3Input.txt")
