from queue import Queue
from threading import Thread

def index(register):
    return ord(register)-ord('a')

def isinteger(str):
    if (str[0] == '-'):
        return True
    else:
        return str.isdigit()

def getTarget(operand, registers):
    if isinteger(operand):
        return int(operand)
    else:
        return registers[index(operand)]

def setV(instruction, registers, opCount):
    registers[index(instruction[1])] = getTarget(instruction[2], registers)
    opCount[0] += 1

def sub(instruction, registers, opCount):
    registers[index(instruction[1])] -= getTarget(instruction[2], registers)
    opCount[1] += 1

def mul(instruction, registers, opCount):
    registers[index(instruction[1])] *= getTarget(instruction[2], registers)
    opCount[2] += 1

def readInput(fileName):
    allInstructions = []
    with open(fileName, 'r') as file:
        for eachLine in file:
            allInstructions.append(eachLine.strip().split(' '))
    return allInstructions

def runProg(instructions):
    specials = set(['jnz'])
    ops = {
        'set': setV,
        'sub': sub,
        'mul': mul,
    }
    registers = [0 for i in range(8)]
    opCounters = {
        0:0,
        1:0,
        2:0,
    }
    i = 0
    while i != len(instructions):
        instruction = instructions[i]
        if instruction[0] in specials:
            if instruction[0] == 'jnz':
                jump = getTarget(instruction[2], registers)
                if getTarget(instruction[1], registers) != 0:
                    i += jump
                else:
                    i+=1
        else:
            ops[instruction[0]](instruction, registers, opCounters)
            i+=1
    return opCounters[2]

def runProg2(instructions):
    b = 81
    c = 81
    b = b * 100 + 100000
    c = b + 17000
    h = 0
    for x in range(b, c + 1, 17):
        if not prime(x):
            h += 1
    return h

def Solution1():
    return runProg(readInput("day23Input.txt"))

def Solution2():
    return runProg2(readInput('day23Input.txt'))

def prime(n):
    if n > 1:
        # check for factors
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return True

print(Solution2())
