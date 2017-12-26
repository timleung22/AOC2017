import sys
def manhattanDist(pointA, pointB):
    return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1]) + abs(pointA[2]-pointB[2])

def parse(input):
    #input in format of P=<X,Y,Z>
    stripped = input[3:-1]
    xyz = []
    for eachN in stripped.split(','):
        xyz.append(int(eachN))
    return xyz

def readInput(fileName):
    positions = []
    velocities = []
    accelerations = []
    with open(fileName, 'r') as file:
        for eachLine in file:
            eachParticle = eachLine.strip().split(', ')
            positions.append(parse(eachParticle[0]))
            velocities.append(parse(eachParticle[1]))
            accelerations.append(parse(eachParticle[2]))

    return positions, velocities, accelerations

def calculateParticle(position, velocity, acceleration, runs):
    for i in range(runs):
        velocity[0] += acceleration[0]
        velocity[1] += acceleration[1]
        velocity[2] += acceleration[2]
        position[0] += velocity[0]
        position[1] += velocity[1]
        position[2] += velocity[2]

    return [position[0], position[1], position[2]], [velocity[0], velocity[1], velocity[2]], acceleration

def merging(arr):
    if len(arr) < 10:
        return False
    else:
        return arr[-1] == arr[-2] and arr[-2] == arr[-3] and arr[-3] == arr[-4] and arr[-4] == arr[-5]


def findClosest(positions, velocities, accelerations):
    origin = [0,0,0]
    nearestParticles = []

    for iter in range(100):
        distances = []
        newPositions, newVelocities, newAccelerations = [], [], []
        for i in range(len(positions)):
            newP, newV, newA = calculateParticle(positions[i], velocities[i], accelerations[i], 5)
            newPositions.append(newP)
            newVelocities.append(newV)
            newAccelerations.append(newA)
            distances.append(manhattanDist(newP, origin))

        newClosestDistance = min(distances)
        for i in range(len(distances)):
            if distances[i] == newClosestDistance:
                nearestParticles.append(i)
        positions = newPositions
        velocities = newVelocities
        accelerations = newAccelerations

    return nearestParticles

def formatPosition(newP):
    return ','.join(str(p) for p in newP)

def removeCollided(positions, velocities, accelerations):
    allPos = []
    for iter in range(500):
        uniquePositions = set()
        newPositions, newVelocities, newAccelerations = [], [], []
        collided = set()
        for i in range(len(positions)):
            newP, newV, newA = calculateParticle(positions[i], velocities[i], accelerations[i], 1)
            formattedPosition = formatPosition(newP)
            if formattedPosition not in uniquePositions:
                uniquePositions.add(formattedPosition)
                newPositions.append(newP)
                newVelocities.append(newV)
                newAccelerations.append(newA)
            else:
                collided.add(formatPosition(newP))

        nextIterPositions, nextIterVelocities, nextIterAccelerations = [], [],[]
        for i in range(len(newPositions)):
            if formatPosition(newPositions[i]) not in collided:
                nextIterPositions.append(newPositions[i])
                nextIterVelocities.append(newVelocities[i])
                nextIterAccelerations.append(newAccelerations[i])
        positions = nextIterPositions
        velocities = nextIterVelocities
        accelerations = nextIterAccelerations
        allPos.append(len(positions))

    return allPos



def Solution1():
    positions, velocities, accelerations = readInput('day20Input.txt')
    return findClosest(positions, velocities, accelerations)

def Solution2():
    positions, velocities, accelerations = readInput('day20Input.txt')
    return removeCollided(positions, velocities, accelerations)

print(Solution2())









