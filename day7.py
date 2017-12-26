class Program(object):
    def __init__(self, name, weight):
        self.children = set()
        self.weight = weight
        self.name = name
        self.balanced = True
        self.totalWeight = self.weight

    def addChild(self, child):
        self.children.add(child)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.name == self.name
        else:
            return False

    def _ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.name.__hash__()

Programs = set()
AllLines = []
AllPrograms = {}

def readInput(file):
    with open(file, "r") as f:
        for eachLine in f:
            eachLine = eachLine.strip()
            AllLines.append(eachLine)

def process():
    for eachLine in AllLines:
        parsed = parseEachLine(eachLine)
        if parsed[0] in Programs:
            Programs.remove(parsed[0])
        else:
            Programs.add(parsed[0])
        for eachTop in parsed[2]:
            if eachTop in Programs:
                Programs.remove(eachTop)
            else:
                Programs.add(eachTop)


def buildGraph():
    for eachLine in AllLines:
        parsed = parseEachLine(eachLine)
        AllPrograms[parsed[0]] = Program(parsed[0], parsed[1])

    for eachLine in AllLines:
        parsed = parseEachLine(eachLine)
        thisProgram = AllPrograms[parsed[0]]
        if len(parsed[2]) != 0:
            for eachChild in parsed[2]:
                thisProgram.addChild(AllPrograms[eachChild])

def processGraph():
    root = AllPrograms["vtzay"] #found this in part 1
    processTotalWeight(root)
    baseWeight = list(filter(lambda c: c.balanced, root.children))[0].totalWeight
    unbalancedWeight = list(filter(lambda c: not c.balanced, root.children))[0].totalWeight
    offset = baseWeight - unbalancedWeight

    return findCorrectedWeight(root, offset)

def processTotalWeight(node):
    for eachChild in node.children:
        processTotalWeight(eachChild)
        node.totalWeight += eachChild.totalWeight
        node.balanced = node.balanced and eachChild.balanced

    if node.balanced and len(node.children) > 0:
        allChildrenWeights = [child.totalWeight for child in node.children]
        node.balanced = max(allChildrenWeights) == min(allChildrenWeights)

def findCorrectedWeight(node, offset):

    weights = []
    for eachChild in node.children:
        weights.append(eachChild.weight)
        if not eachChild.balanced:
            return findCorrectedWeight(eachChild, offset)

    # if here, that means I am marked as not Balanced but all my children are balance.  That means,
    # one of my children has a weight that is off by offset.
    return findOutlinerChild(node).weight + offset

def findOutlinerChild(node):
    weights = {}
    for eachChild in node.children:
        if weights.get(eachChild.totalWeight, None) == None:
            weights[eachChild.totalWeight] = [eachChild]
        else:
            weights.get(eachChild.totalWeight).append(eachChild)
    for eachWeight in weights.values():
        if len(eachWeight) == 1:
            return eachWeight[0]
    return None


def parseEachLine(eachLine):
    bottomPart = eachLine
    topNames = []
    if "->" in eachLine:
        arrowIndex = eachLine.index("->")
        bottomPart = bottomPart[0:arrowIndex-1]
        topPart = eachLine[arrowIndex+3:].strip()
        for eachTop in topPart.split(","):
            topNames.append(eachTop.strip())

    bottomWeightIdx = bottomPart.index("(")
    bottomName = bottomPart[0:bottomWeightIdx-1]
    bottomWeight = int(bottomPart[bottomWeightIdx+1:-1])

    return (bottomName, bottomWeight, topNames)

#print(parseEachLine("dihjv (2158) -> gausx, ncdmp, hozgrub"))
#print(parseEachLine("eauol (56)"))

def Solution1():
    readInput("day7Input.txt")
    process()
    print(Programs)

def Solution2():
    readInput("day7Input.txt")
    buildGraph()
    return processGraph()

print(Solution2())



