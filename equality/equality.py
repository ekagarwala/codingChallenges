import os
import re


os.chdir("e:\\repos\\codingChallenges\\data")

message = ''
possibilities = []
with open('../data/equality.txt', 'r') as inFile:
    inText = inFile.readlines()

pat = re.compile("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z, \n]")
for line in inText:
    match = re.search(pat, line)
    if match is not None:
        message += line[match.span()[0] + 4]
        possibilities.append(line[match.span()[0]:match.span()[1]])

print message
