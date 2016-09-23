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
