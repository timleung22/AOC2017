from utils import readInput

Registers = {}

def eq(reg, val):
    return Registers[reg] == val

def neq(reg, val):
    return not eq(reg, val)

def largerEqual(reg, val):
    return Registers[reg] >= val

def smallerEqual(reg, val):
    return Registers[reg] <= val

def larger(reg, val):
    return not smallerEqual(reg, val)

def smaller(reg, val):
    return not largerEqual(reg, val)

def runConditions(reg, op, value):
    conditions = {
        '==' : eq,
        '!=' : neq,
        '<' : smaller,
        '<=' : smallerEqual,
        '>' : larger,
        '>=' : largerEqual,
    }
    return conditions[op](reg, value)

def runLine(splittedLine, highestSeen):
    v = highestSeen
    if (runConditions(splittedLine[4], splittedLine[5], int(splittedLine[6]))):
        if splittedLine[1] == 'inc':
            Registers[splittedLine[0]] += int(splittedLine[2])
        elif splittedLine[1] == 'dec':
            Registers[splittedLine[0]] -= int(splittedLine[2])
        else:
            raise Exception('Unknown Opertion' + splittedLine[1])
        v = Registers[splittedLine[0]]
    return v

def Solution1():
    lines = readInput("day8Input.txt")
    for eachLine in lines:
        splitted = eachLine.split(' ')
        Registers[splitted[0]] = 0

    highestValue = 0
    for eachLine in lines:
        splitted = eachLine.split(' ')
        lineResult = runLine(splitted, highestValue)
        if lineResult > highestValue:
            highestValue = lineResult

    return (max(Registers.values()), highestValue)

print(Solution1())


