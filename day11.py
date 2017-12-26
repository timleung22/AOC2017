def north(pos):
    return (pos[0], pos[1]+1, pos[2]-1)

def northeast(pos):
    return (pos[0]+1, pos[1], pos[2]-1)

def southeast(pos):
    return(pos[0]+1, pos[1]-1, pos[2])

def south(pos):
    return (pos[0], pos[1]-1, pos[2]+1)

def southwest(pos):
    return (pos[0]-1, pos[1], pos[2]+1)

def northwest(pos):
    return(pos[0]-1, pos[1]+1, pos[2])

moveDir = {
    'n': north,
    'ne': northeast,
    'se': southeast,
    's': south,
    'sw': southwest,
    'nw': northwest,
}

class Navigator(object):
    def __init__(self):
        self.pos = (0,0,0)
        self.distance = 0
        self.maxDistance = 0
        self.furthest = (0,0,0)

    def move(self, direction):
        self.pos = moveDir[direction](self.pos)
        self.calDistance()

    def calDistance(self):
        self.distance = abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        if self.distance > self.maxDistance:
            self.maxDistance = self.distance
            self.furthest = self.pos

    def findSteps(self, pos):
        absPos = [abs(pos[i]) for i in range(len(pos))]
        return max(absPos)

def navigate(steps):
    nav = Navigator()
    for step in steps:
       nav.move(step)
    return nav

def Solution1():
    steps = []
    with open("day11Input.txt", 'r') as f:
        line = f.readline()
        for eachStep in line.strip().split(','):
            steps.append(eachStep)

    return navigate(steps)

result = Solution1()
print(result.pos)
print(result.distance)
print(result.maxDistance)
print(result.furthest)
print(result.findSteps(result.pos))
print(result.findSteps(result.furthest))