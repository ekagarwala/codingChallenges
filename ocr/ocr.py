import os
from collections import defaultdict


os.chdir("e:\\repos\\codingChallenges\\ocr\\data")
characters = defaultdict(int)
fileName = 'inputString.txt'


with open(fileName, 'r') as file:
    for line in file:
        for x in line:
            if not x == "\n":
                characters[x] += 1


valid = [k for k, v in characters.items() if v == 1]

orderedOutput = []
with open(fileName, 'r') as file:
    for line in file:
        for x in line:
            if x in valid:
                orderedOutput.append(x)

print ''.join(orderedOutput)
