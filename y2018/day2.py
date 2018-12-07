def setUpCounts(line):
    letterCount = []
    for i in range(26):
        letterCount.append(0)

    for eachC in line:
        letterCount[ord(eachC) - ord('a')] += 1
    return letterCount

def Solution1(input):
    hasTwo = 0
    hasThree = 0

    with open(input, "r") as f:
        for eachLine in f:
            letterCount = setUpCounts(eachLine[:-1])
            hasTwoCheck = False
            hasThreeCheck = False
            for eachCount in letterCount:
                hasTwoCheck = hasTwoCheck or (eachCount == 2)
                hasThreeCheck = hasThreeCheck or (eachCount == 3)
            if hasTwoCheck:
                hasTwo += 1
            if hasThreeCheck:
                hasThree += 1

    print(hasTwo*hasThree)

def diffOne(first, second):
    diff = 0
    for x, eachC in enumerate(first):
        if second[x] != eachC:
            diff += 1
            if (diff > 1):
                return False

    return (diff == 1)


def commonChars(first, second):
    common = []
    for x, eachC in enumerate(first):
        if second[x] == eachC:
            common.append(eachC)
    return ''.join(common)

def Solution2(input):
    inputArr = []
    with open(input, "r") as f:
        for eachLine in f:
            inputArr.append(eachLine[:-1])

    done = False
    for x in range(len(inputArr)):
        if not done:
            for y in range(x+1, len(inputArr)):
                if (diffOne(inputArr[x], inputArr[y])):
                    print(commonChars(inputArr[x], inputArr[y]))
                    done = True
                    break


Solution2("day2input.txt")


