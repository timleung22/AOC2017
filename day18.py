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

def setV(instruction, registers):
    registers[index(instruction[1])] = getTarget(instruction[2], registers)

def add(instruction, registers):
    registers[index(instruction[1])] += getTarget(instruction[2], registers)

def mul(instruction, registers):
    registers[index(instruction[1])] *= getTarget(instruction[2], registers)

def mod(instruction, registers):
    v = registers[index(instruction[1])]
    registers[index(instruction[1])] = v % getTarget(instruction[2], registers)

def readInput(fileName):
    allInstructions = []
    with open(fileName, 'r') as file:
        for eachLine in file:
            allInstructions.append(eachLine.strip().split(' '))
    return allInstructions

def runPlaySound(instructions):
    specials = set(['snd', 'rcv', 'jgz'])
    ops = {
        'set': setV,
        'add': add,
        'mul': mul,
        'mod': mod,
    }
    registers = [0 for i in range(26)]
    lastPlayed = 0
    recovered = False
    i = 0
    while not recovered:
        instruction = instructions[i]
        if instruction[0] in specials:
            if instruction[0] == 'snd':
                lastPlayed = registers[index(instruction[1])]
                i+=1
            elif instruction[0] == 'rcv':
                if getTarget(instruction[1], registers) != 0:
                    recovered = True
                    i+=1
            else:
                jump = getTarget(instruction[2], registers)
                if registers[index(instruction[1])] > 0:
                    i += jump
                else:
                    i+=1
        else:
            ops[instruction[0]](instruction, registers)
            i+=1
    return lastPlayed

def run(instructions, registers, myMessageQueue, targetMessageQueue, id):
    specials = set(['snd', 'rcv', 'jgz'])
    ops = {
        'set': setV,
        'add': add,
        'mul': mul,
        'mod': mod,
    }

    i = 0
    sent = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction[0] in specials:
            if instruction[0] == 'snd':
                targetMessageQueue.put(getTarget(instruction[1], registers))
                sent += 1
                i += 1
            elif instruction[0] == 'rcv':
                print("Thread " + str(id) + "sent " + str(sent))
                registers[index(instruction[1])] = myMessageQueue.get()
                i += 1
            else:
                jump = getTarget(instruction[2], registers)
                if getTarget(instruction[1], registers) > 0:
                    i += jump
                else:
                    i += 1
        else:
            ops[instruction[0]](instruction, registers)
            i += 1
    print("Thread " + str(id) + "sent " + str(sent))

def Solution1():
    return runPlaySound(readInput("day18Input.txt"))

def Solution2():
    instructions = readInput("day18Input.txt")
    registersP0 = [0 for i in range(26)]
    registersP1 = [0 for i in range(26)]
    registersP1[ord('p')-ord('a')] = 1

    p0Queue = Queue()
    p1Queue = Queue()
    threadA = Thread(target=run, args=(instructions, registersP0, p0Queue, p1Queue, 0))
    threadB = Thread(target=run, args=(instructions, registersP1, p1Queue, p0Queue, 1))


    threadA.start()
    threadB.start()

Solution2()