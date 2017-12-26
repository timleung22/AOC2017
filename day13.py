import copy
def readInput(fileName):
    lines = {}
    with open(fileName, 'r') as file:
        for eachLine in file:
            tokens = eachLine.strip().split(":")
            lines[int(tokens[0].strip())] = int(tokens[1].strip())-1
    return lines

def initFirewall(depthAndRange):
    totalDepth = max(depthAndRange.keys())
    firewall = [depthAndRange.get(i, 0) for i in range(totalDepth+1)]
    return firewall

def move(scannerPos, scannerDir, firewall, cont):
    totalS = 0
    for i in range(len(firewall)):
        if scannerPos[i] == 0 and firewall[i] != 0:
            totalS += i*(firewall[i]+1)
            if not cont and totalS > 0:
                return totalS
        moveScanner(scannerPos, scannerDir, firewall)
    return totalS

def moveScanner(scannerPos, scannerDir, firewall):
    for j in range(len(firewall)):
        if firewall[j] != 0:
            scannerPos[j] += scannerDir[j]

            if scannerDir[j] == 1 and scannerPos[j] == firewall[j]:
                scannerDir[j] = -1
            if scannerDir[j] == -1 and scannerPos[j] == 0:
                scannerDir[j] = 1

def initScanners(delay, firewall):
    scannerPos = [0 for i in range(len(firewall))]
    scannerDir = [1 for i in range(len(firewall))]
    for i in range(delay):
        moveScanner(scannerPos, scannerDir, firewall)
    return (scannerPos, scannerDir)

def Solution1():
    firewall = initFirewall(readInput('day13Input.txt'))
    scannerPos, scannerDir = initScanners(0, firewall)
    print(move(scannerPos, scannerDir, firewall, True))

def Solution2():
    firewall = initFirewall(readInput('day13Input.txt'))
    scannerPos, scannerDir = initScanners(0, firewall)
    severity = move(copy.deepcopy(scannerPos), copy.deepcopy(scannerDir), firewall, False)
    delay = 0
    while severity != 0:
        delay += 1
        moveScanner(scannerPos, scannerDir, firewall)
        severity = 1 if scannerPos[0] == 0 else move(copy.deepcopy(scannerPos), copy.deepcopy(scannerDir), firewall, False)
    print(delay)

Solution1()
Solution2()

