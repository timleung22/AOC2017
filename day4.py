def Solution1(input):
    validCount = 0

    with open(input, "r") as f:
        for i, eachLine in enumerate(f):
            if validPassPhrase1(eachLine):
                validCount += 1
    return validCount


def validPassPhrase1(line):
    dictionary = set()
    count = 0
    for eachWord in line.strip().split(" "):
        dictionary.add(eachWord)
        count += 1
    return count == len(dictionary)


def Solution2(input):
    validCount = 0

    with open(input, "r") as f:
        for i, eachLine in enumerate(f):
            if validPassPhrase2(eachLine):
                validCount += 1
    return validCount

def validPassPhrase2(line):
    dictionary = set()
    count = 0
    for eachWord in line.strip().split(" "):
        dictionary.add(''.join(sorted(set(eachWord.strip()))))
        count += 1
    return count == len(dictionary)

