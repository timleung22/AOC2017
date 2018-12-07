def Solution1(input):
    sum = 0

    with open(input, "r") as f:
        for i, eachLine in enumerate(f):
            sum += int(eachLine)
    print(sum)

def Solution2(input):
    frequencies = set()
    current = 0
    inputs = []

    with open(input, "r") as f:
        for eachLine in f:
            inputs.append(int(eachLine))

    i = 0
    while(True):
        current += inputs[i % len(inputs)]
        i += 1
        if current in frequencies:
            print(current)
            break
        frequencies.add(current)





Solution2("day1Input.txt")
