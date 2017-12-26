import urllib.request
import re

def mdist(p, q):
    dist = 0
    for i, j in zip(p, q):
        dist += abs(i - j)
    return dist

def readInput(file):
    lines = []
    with open(file, "r") as f:
        for eachLine in f:
            eachLine = eachLine.strip()
            lines.append(eachLine)

    return lines

def regexPattern(regex):
    return re.compile(regex, re.VERBOSE)

def readAndParseInput(file, regex):
    lines = []
    pattern = regexPattern(regex)
    with open(file, "r") as f:
        for eachLine in f:
            eachLine = eachLine.strip()
            lines.append(pattern.match(eachLine))
    return lines


