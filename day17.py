def Solution1(steps, target):
    buffer = [0]
    currStep = 0
    for i in range(target):
        forward = steps % len(buffer)
        movedTo = (currStep + forward) % len(buffer)
        buffer = buffer[:movedTo+1] + [i+1] + buffer[movedTo+1:]
        print(buffer)
        currStep = movedTo+1
    return buffer[buffer.index(target)+1]

#print(Solution1(303, 2017))

def Solution2(steps, target):
    # instead of actually doing all those things in Solution 1, we just need to worry about:
    # position of 0 is always 0
    # number at position 1
    # length of the buffer
    # currentPosition 
    context = [1, 2, 1] # value at buffer[1], len of buffer, currentStep
    for i in range(1, target):
        forward = steps % context[1]
        movedTo = (context[2]+forward) % context[1]
        if movedTo == 0:
            context[0] = i+1 # inserted new value next to 0
        context[2] = movedTo+1
        context[1] += 1
    return context[0]

print(Solution2(303, 50000000))



