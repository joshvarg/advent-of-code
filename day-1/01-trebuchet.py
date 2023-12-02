# Objective:
# Isolate the first digit and the last digit to form a single two-digit number

import sys
import re
#filename = sys.argv[1]
#f = open(filename)
d = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
        "zero" : "0"
        }
w = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def FirstWordSearch(line):
    firstIndex = len(line)
    firstNum = "null"
    for word in w:
        match = list(re.finditer(word, line))
        if (len(match) > 0 and match[0].start() < firstIndex):
            firstIndex = match[0].start()
            firstNum = match[0].group()
    if (firstNum != "null"):
        return (d[firstNum], firstIndex)
    else:
        return (0, len(line))

def LastWordSearch(line):
    lastIndex = 0
    lastNum = "null"
    for word in w:
        match = list(re.finditer(word, line))
        if (len(match) > 0 and match[-1].start() > lastIndex):
            lastIndex = match[-1].start()
            lastNum = match[-1].group()
    if (lastNum != "null"):
        return (d[lastNum], lastIndex)
    else:
        return ("-1", -1)

def FirstIntegerSearch(line):
    i = 0
    firstDigit = line[i]
    isNotFirstDigit = True
    while(isNotFirstDigit):
        if(firstDigit.isnumeric() or i >= len(line) - 1):
            isNotFirstDigit = False
        else:
            i += 1
            firstDigit = line[i]
    return (firstDigit, i)

def LastIntegerSearch(line):
    j = len(line) - 1
    lastDigit = line[j]
    isNotLastDigit = True
    while(isNotLastDigit):
        if(lastDigit.isnumeric() or j <= 0):
            isNotLastDigit = False
        else:
            j -= 1
            lastDigit = line[j]
    return (lastDigit, j)

def main():
    filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()

    count = 0
    for line in lines:
        fwt = FirstWordSearch(line)
        lwt = LastWordSearch(line)
        fit = FirstIntegerSearch(line)
        lit = LastIntegerSearch(line)

        num = ""

        if (fwt[1] < fit[1]):
            num += fwt[0]
        else:
            num += fit[0]

        if (lwt[1] > lit[1]):
            num += lwt[0]
        else:
            num += lit[0]
        count += int(num)

    return count
print(main())
