import timeit

def swap(str, x, y):
    c = str[x]
    str[x] = str[y]
    str[y] = c
    return str

def exchange(str, operands):
    slash = operands.index("/")
    x = int(operands[0:slash])
    y = int(operands[slash+1:])
    return swap(str, x, y)

def partner(str, operands):
    slash = operands.index("/")
    p = operands[:slash]
    q = operands[slash+1:]
    return swap(str, str.index(p), str.index(q))

def spin(str, operands):
    n = int(operands)
    return str[-n:] + str[0:len(str)-n]

def runCommands(raw, commands):
    for eachCommand in commands:
        raw = processCommand(raw, eachCommand)
    return raw

def Solution1(loops):
    seen = []
    raw = [chr(i+ord('a')) for i in range(0, 16)]
    commands = []
    with open("day16Input.txt", 'r') as file:
        commands = file.readline().strip().split(',')
    for i in range(loops):
        check = ''.join(raw)
        if check in seen:
            return seen[loops % i]
        seen.append(check)
        raw = runCommands(raw, commands)
    return ''.join(raw)

def applyTransformation(arr, transformation):
    out = ['' for i in range(len(arr))]
    for i in range(len(arr)):
        out[transformation[i]] = arr[i]
    return out



def runSpin(arr, operand):
    n = int(operand)
    for i in range(len(arr)):
        arr[i] = (arr[i]+n)%16

def runExchange(arr, operands):
    slash = operands.index("/")
    x = int(operands[0:slash])
    y = int(operands[slash+1:])
    xpos, ypos = 0, 0
    for i in range(len(arr)):
        if arr[i] == x:
            xpos = i
    for i in range(len(arr)):
        if arr[i] == y:
            ypos = i
    arr[xpos] = y
    arr[ypos] = x

def runPartner(arr, operands):
    slash = operands.index("/")
    xpos = ord(operands[0:slash])-ord('a')
    ypos = ord(operands[slash+1:])-ord('a')
    temp = arr[xpos]
    arr[xpos] = arr[ypos]
    arr[ypos] = temp



def run(arr, command):
    ops = {
        "s" : runSpin,
        "x" : runExchange,
        "p" : runPartner,
    }
    ops[command[0]](arr, command[1:])

def processCommand(str, command):
    ops = {
        's': spin,
        'x': exchange,
        'p': partner,
    }
    return ops[command[0]](str, command[1:])

print(Solution1(1))
print(Solution1(2))
print(Solution1(1000000000))