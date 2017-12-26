def readInput(fileName):
    programsMap = {}
    with open(fileName, 'r') as file:
        for eachLine in file:
            eachLine = eachLine.strip()
            pipe = eachLine.index("<->")
            source = int(eachLine[:pipe-1])
            targets = eachLine[pipe+4:]
            allTargets = []
            for eachTarget in targets.split(","):
                allTargets.append(int(eachTarget))

            programsMap[source] = allTargets
    return programsMap

def findReachables(targets, seen, programsMap):
    for target in targets:
        if target not in seen:
            seen.add(target)
            findReachables(programsMap[target], seen, programsMap)

def Solution1():
    programs = readInput("day12Input.txt")
    directComms = programs[0]
    friendsOfZero = set()
    friendsOfZero.add(0)
    findReachables(directComms, friendsOfZero, programs)
    print(len(friendsOfZero))

def Solution2():
    programs = readInput("day12Input.txt")
    processed = set()
    groups = 0
    for source in programs.keys():
        if source not in processed:
            processed.add(source)
            findReachables(programs[source], processed, programs)
            groups += 1
    print(groups)

Solution1()
Solution2()




