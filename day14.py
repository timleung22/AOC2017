from functools import reduce
import sys

def getHashInput(key):
    hashInput = []
    for eachC in key:
        hashInput.append(ord(eachC))
    return hashInput + [17, 31, 73, 47, 23]

def initArray():
    return [i for i in range(256)]

def knotHash(hashInput):
    current = 0
    skip = 0
    arr = initArray()
    for iteration in range(64):
        for eachLength in hashInput:
            arr = processArray(arr, current, eachLength)
            current = (current+eachLength+skip) % len(arr)
            skip += 1

    denseHarshed = denseHarsh(arr)
    return printDenseHarsh(denseHarshed)

def processArray(arr, current, length):
    if current + length > len(arr):
        subArr = (arr[current:] + arr[:(current+length)%len(arr)])[::-1]
        return subArr[len(arr)-current:] + arr[current+length-len(arr):current] + subArr[:len(arr)-current]
    else:
        subArr = (arr[current:current+length])[::-1]
        return arr[:current] + subArr + arr[current+length:]

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

def convertToBinary(hexString):
    scale = 16  ## equals to hexadecimal
    num_of_bits = 128
    return bin(int(hexString, scale))[2:].zfill(num_of_bits)


def getOutputGrid():
    key = "ljoxqyyw"
    hashOutputs = []
    for i in range(128):
        hashInput = getHashInput(key+"-"+str(i))
        hashOutputs.append(knotHash(hashInput))

    binOutputs = []
    for eachHashOut in hashOutputs:
        binOut = str(convertToBinary(eachHashOut))
        binOutputs.append(binOut)
    return binOutputs

def Solution1():
    binOutputs = getOutputGrid()
    totalOnes = 0
    for eachLine in binOutputs:
        for eachC in eachLine:
            if eachC == '1':
                totalOnes += 1
    print(totalOnes)

def Solution2():
    grid = getOutputGrid()
    regions = [[0 for col in range(128)] for row in range(128)]
    color = 0
    highestColor = color
    for row in range(128):
        for col in range(128):
            if grid[row][col] == '1':
                color = getColor(highestColor, row, col, grid, regions)
                if color > highestColor:
                    highestColor = color
                regions[row][col] = color

    printGrid(regions)
    print("*************")
    maxRegion = findRegionsCount(regions)
    count = 1
    while True:
        merged = mergeRegions(regions)
        mergedMaxRegion = findRegionsCount(merged)
        count += 1
        if mergedMaxRegion == maxRegion and findSum(merged) == findSum(regions):
            nonZero = 0
            for eachRow in merged:
                for eachN in eachRow:
                    if eachN != 0:
                        nonZero += 1
            printGrid(merged)
            print(nonZero)
            print(mergedMaxRegion)
            break
        else:
            regions = merged
            maxRegion = mergedMaxRegion


def getColor(seedColor, i, j, grid, regions):
    if seedColor == 0:
        return 1
    if not j == 0:
        if grid[i][j-1] == '1':
            return regions[i][j-1]
        else:
            return seedColor+1
    if not i == 0:
        if grid[i-1][j] == '1':
            return regions[i-1][j]
        else:
            return seedColor+1

def mergeRegions(regions, size = 128):
    updatedRegions = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            updatedRegions[i][j] = findColor(i, j, regions, size)
    return updatedRegions

def findColor(i, j, regions, size):
    if regions[i][j] == 0:
        return 0
    else:
        candidates = [regions[i][j]]
        if i != 0 and regions[i-1][j] != 0:
            candidates.append(regions[i-1][j])
        if i != size-1 and regions[i+1][j] != 0:
            candidates.append(regions[i+1][j])
        if j != 0 and regions[i][j-1] != 0:
            candidates.append(regions[i][j-1])
        if j != size-1 and regions[i][j+1] != 0:
            candidates.append(regions[i][j+1])
        return min(candidates)

def printGrid(grid):
    for eachLine in grid:
        line = ""
        for eachN in eachLine:
            line += str(eachN).ljust(5)
        print(line)

def findRegionsCount(regions):
    candidates = set()
    for eachRow in regions:
        for eachN in eachRow:
            if not eachN in candidates and eachN != 0:
                candidates.add(eachN)
    return len(candidates)

def findSum(regions):
    rowSum = []
    for eachRow in regions:
        rowSum.append(reduce(lambda x,y: x+y, eachRow))
    return reduce(lambda x,y: x+y, rowSum)

Solution2()







