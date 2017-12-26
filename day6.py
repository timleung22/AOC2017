import copy

def reallocation(input):
    numbers = copy.copy(input)
    maxBlock = max(numbers)
    for i, eachBlock in enumerate(numbers):
        if eachBlock == maxBlock:
            numbers[i] = 0
            realloc = i+1
            while maxBlock > 0:
                numbers[realloc % len(numbers)] += 1
                maxBlock -= 1
                realloc += 1

    return numbers

def findInstructions(input, producedOutputs):
    steps = 0
    reallocated = input
    lastConfig = ','.join(str(x) for x in reallocated)
    while lastConfig not in producedOutputs.keys():
        producedOutputs[lastConfig] = steps
        reallocated = reallocation(reallocated)
        lastConfig = ','.join(str(x) for x in reallocated)
        steps += 1
    return steps - producedOutputs[lastConfig]

def Solution1(inputFile):
    banks = []
    with open(inputFile, "r") as f:
        for eachLine in f:
            splitted = eachLine.strip().split("\t")
            for eachSplitted in splitted:
                banks.append(int(eachSplitted))

    return findInstructions(banks, {})

print(Solution1("day6Input.txt"))
#print(findInstructions([0,2,7,0], {}))
