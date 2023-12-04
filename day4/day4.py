def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines

def getformatedinput():
    lines = readInput("day4//input.txt")
    formated = []
    for line in lines:
        tmp = line.split(":",1)[1].split(" |",1)
        tmp2 = []
        tmp2.append(tmp[0].split())
        tmp2.append(tmp[1].split())
        formated.append(tmp2)
    return formated

def task1():
    input = getformatedinput()
    sum = 0
    for line in input:
        val = 0.5
        for winnum in line[0]:
            if winnum in line[1]:
                val *= 2
        sum += int(val)
    print(str(sum))

def initialize(val, length):
    res = []
    for i in range(length):
        res.append(val)
    return res

def task2():
    input = getformatedinput()
    sum = 0
    count = initialize(1, len(input))
    for i in range(len(input)):
        n = 0
        for winnum in input[i][0]:
            if winnum in input[i][1]:
                n += 1
        for j in range(n):
            count[i+j+1] += count[i]
        sum += count[i]
    print(str(sum))

task1()
task2()