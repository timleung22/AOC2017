import re
import operator

#[1518-10-14 23:57] Guard #2377 begins shift
shiftPattern = re.compile(r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.*) #([0-9]+) (.*) (.*)")
sleepsPattern = re.compile(r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] falls asleep")
wakesPattern = re.compile(r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] wakes up")
daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

eventLog = []
inputs = {}

def initEventLog():
    for x in range(365):
        timelog = []
        for t in range(60):
            timelog.append(0)
        eventLog.append((0, timelog))

def parseLine(line):
    if '#' in line:
        shiftLine(line)
    elif 'falls' in line:
        sleepsLine(line)
    else:
        wakesLine(line)

def shiftLine(line):
    matches = shiftPattern.search(line)
    month = matches.group(2)
    day = matches.group(3)
    hour = matches.group(4)
    min = matches.group(5)
    guard = strToInt(matches.group(7))
    addToInput(month, day, hour, min, guard, 1)

def sleepsLine(line):
    matches = sleepsPattern.search(line)
    month = matches.group(2)
    day = matches.group(3)
    hour = matches.group(4)
    min = matches.group(5)
    addToInput(month, day, hour, min, 0, 0)

def wakesLine(line):
    matches = wakesPattern.search(line)
    month = matches.group(2)
    day = matches.group(3)
    hour = matches.group(4)
    min = matches.group(5)
    addToInput(month, day, hour, min, 0, 1)

def strToInt(str):
    if str[0] == '0':
        return int(str[1])
    else:
        return int(str)

def monthDayToIndex(month, day, hour, min):
    monthInt = strToInt(month)
    dayInt = strToInt(day)

    index = 0
    for i in range(monthInt):
        index += daysInMonth[i]
    index += (dayInt - 1)
    if strToInt(hour) != 0:
        index += 1
        return (index, 0)
    else:
        return (index, strToInt(min))


def addToInput(month, day, hour, min, guard, state):
    inputs[month+day+hour+min] = (month, day, hour, min, guard, state)

def fillEventLog(month, day, hour, min, guard, state):
    (index, minStart) = monthDayToIndex(month, day, hour, min)
    log = eventLog[index][1]
    for i in range(minStart, 60):
        log[i] = state
    assignedGuard = guard if guard != 0 else eventLog[index][0]
    eventLog[index] = (assignedGuard, log)

def Solution1():
    initEventLog()
    with open("day4Input.txt", "r") as f:
        for eachLine in f:
            parseLine(eachLine)

    sortedInputs = sorted(inputs.items(), key=operator.itemgetter(0))

    for eachInput in sortedInputs:
        inputLine = eachInput[1]
        fillEventLog(inputLine[0], inputLine[1], inputLine[2], inputLine[3], inputLine[4], inputLine[5])

    for eachLine in eventLog:
        print('{0:5d} : {1}'.format(eachLine[0], eachLine[1]))

Solution1()