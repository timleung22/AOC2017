diff = abs(ord('A') - ord('a'))

def processChar(line, c):
    if len(line) == 0:
        line += c
    elif canCancel(line[-1], c):
        line = line[:-1]
    else:
        line += c

    return line

def canCancel(c1, c2):
    if abs(ord(c1) - ord(c2)) == diff:
        return True
    else:
        return False

def readInputLine(input):
    line = ""
    with open(input, "r") as f:
        for eachLine in f:
            line += eachLine.strip()
    return line

def strip(line, c):
    result = ''
    v = ord(c)
    for eachC in line:
        if c != eachC.lower():
            result += eachC
    return result

def Solution1(input):
    line = readInputLine("day5Input.txt")

    result = ""
    for eachC in line:
        result = processChar(result, eachC)
    print(len(result))

def Solution2(input):
    line = readInputLine("day5Input.txt")
    reducedSizes = []
    for i in range(ord('z')-ord('a')):
        reducedLine = strip(line, chr(ord('a')+i))
        #print("*** " + str(len(reducedLine)))
        reacted = ""
        for eachC in reducedLine:
            reacted = processChar(reacted, eachC)
        reducedSizes.append(len(reacted))

    print(min(reducedSizes))

Solution1("day5Input.txt")
Solution2("day5Input.txt")

