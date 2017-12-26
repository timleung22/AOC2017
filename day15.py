def genMatch(seedA, seedB, rounds, factors=(1,1)):
    totalMatch = 0
    for i in range(rounds):
        genA = genNum(seedA, 16807, factors[0])
        genB = genNum(seedB, 48271, factors[1])
        seedA = genA
        seedB = genB
        totalMatch += findMatch(genA, genB)
    return totalMatch

def genNum(seed, multiplier, factor):
    n = (seed*multiplier)%2147483647
    if n % factor == 0:
        return n
    else:
        return genNum(n, multiplier, factor)


def lower32Bits(val):
    return bin(val)[2:].zfill(32)[16:]

def findMatch(valA, valB):
    if lower32Bits(valA) == lower32Bits(valB):
        return 1
    else:
        return 0

def Solution1():
    print(genMatch(116, 299, 40*1000*1000))

def Solution2():
    print(genMatch(116, 299, 5*1000*1000, (4,8)))

Solution2()