def Solution1(inputFile):
    instructions = []
    with open(inputFile, "r") as f:
        for eachLine in f:
            instructions.append(int(eachLine.strip()))

    curr = 0
    steps = 0
    while (curr < len(instructions) and curr >= 0):
        steps += 1
        next = curr + instructions[curr]
        instructions[curr] = instructions[curr]+1
        curr = next

    return steps

def Solution2(inputFile):
    instructions = []
    with open(inputFile, "r") as f:
        for eachLine in f:
            instructions.append(int(eachLine.strip()))

    curr = 0
    steps = 0
    while (curr < len(instructions) and curr >= 0):
        steps += 1
        offset = instructions[curr]
        instructions[curr] = instructions[curr]+1 if offset < 3 else instructions[curr]-1
        curr = curr+offset

    return steps

print(Solution1("day5Input.txt"))
print(Solution2("day5Input.txt"))