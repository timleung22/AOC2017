from functools import reduce

def testReverse():
    myList = [0,1,2,3,4]
    print(myList[0:3][::-1]+myList[0+3:])

def testSubList(i, n):
    myList = [0,1,2,3,4,5]
    if i+n > len(myList):
        print(myList[i:]+myList[:(i+n)%len(myList)])
    else:
        print(myList[i:i+n])

def readInput(fileName):
    inputs = []
    with open(fileName, 'r') as f:
        line = f.readline().strip()
        for eachN in line.split(","):
            inputs.append(int(eachN))
    return inputs

def readInput2(fileName):
    inputs = []
    with open(fileName, 'r') as f:
        line = f.readline().strip()
        for eachC in line:
            inputs.append(ord(eachC))
    return inputs


def initArray():
    return [i for i in range(256)]

def processArray(arr, current, length):
    if current + length > len(arr):
        subArr = (arr[current:] + arr[:(current+length)%len(arr)])[::-1]
        return subArr[len(arr)-current:] + arr[current+length-len(arr):current] + subArr[:len(arr)-current]
    else:
        subArr = (arr[current:current+length])[::-1]
        return arr[:current] + subArr + arr[current+length:]

def Solution1():
    arr = initArray()
    input = readInput("day10Input.txt")
    current = 0
    skip = 0
    for eachLength in input:
        arr = processArray(arr, current, eachLength)
        current = (current+eachLength+skip)%len(arr)
        skip += 1
        #print(arr)

    return arr[0]*arr[1]

def Solution2():
    arr = initArray()
    input = readInput2("day10Input.txt")
    input = input + [17, 31, 73, 47, 23]
    current = 0
    skip = 0
    for iteration in range(64):
        for eachLength in input:
            arr = processArray(arr, current, eachLength)
            current = (current+eachLength+skip) % len(arr)
            skip += 1

    denseHarshed = denseHarsh(arr)
    return printDenseHarsh(denseHarshed)

def denseHarsh(arr):
    result = []
    for i in range(16):
        begin = i*16
        subArray = arr[begin:begin+16]
        result.append(
            reduce((lambda x, y: x^y), subArray)
        )
    return result

def printDenseHarsh(arr):
    formatted = ""
    for each in arr:
        hexV = str(hex(each))[2:]
        if len(hexV) < 2:
            hexV = '0'+hexV
        formatted = formatted + hexV
    return formatted

def checksum():
    sum = 0
    for i in range(256):
        sum += i

    return sum

def test1():
    inputs = [3,4,1,5]
    arr = [i for i in range(5)]
    current = 0
    skip = 0
    for eachLength in inputs:
        arr = processArray(arr, current, eachLength)
        current = (current+eachLength+skip) % len(arr)
        skip += 1

    print(arr[0]*arr[1])

#print(checksum())
#print(Solution1())
print(Solution2())


