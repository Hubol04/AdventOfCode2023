def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines

def getformatedinput():
    lines = readInput("day7//input.txt")
    formated = []
    for line in lines:
        tmp1 = line.split()
        tmp1.append(-1)
        formated.append(tmp1)
    return formated

def gettype(hand):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for char in hand:
        if char == "2":
            count[0] += 1
        elif char == "3":
            count[1] += 1
        elif char == "4":
            count[2] += 1
        elif char == "5":
            count[3] += 1
        elif char == "6":
            count[4] += 1
        elif char == "7":
            count[5] += 1
        elif char == "8":
            count[6] += 1
        elif char == "9":
            count[7] += 1
        elif char == "T":
            count[8] += 1
        elif char == "J":
            count[9] += 1
        elif char == "Q":
            count[10] += 1
        elif char == "K":
            count[11] += 1
        elif char == "A":
            count[12] += 1
    pairs = 0
    trios = 0
    for n in count:
        if n == 2:
            pairs += 1
        elif n == 3:
            trios += 1
        elif n == 4:
            return 5
        elif n == 5:
            return 6
    if (trios == 1) and (pairs == 1):
        return 4
    elif trios == 1:
        return 3
    elif pairs == 2:
        return 2
    elif pairs == 1:
        return 1
    return 0

def keyfunc(val):
    res = 0
    for i in range(5):
        x = 0
        try:
            x = int(val[0][i])
        except:
            if (val[0][i] == "T"):
                x = 10
            elif (val[0][i] == "J"):
                x = 11
            elif (val[0][i] == "Q"):
                x = 12
            elif (val[0][i] == "K"):
                x = 13
            elif (val[0][i] == "A"):
                x = 14
        res += 100**(5-i)*x
    return res

def task1():
    sum = 0
    input = getformatedinput()
    types = [[], [], [], [], [], [], []]
    for hand in input:
        hand[2] = gettype(str(hand[0]))
        types[hand[2]].append(hand)
    sorted = []
    for type in types:
        type.sort(key = keyfunc)
        for hand in type:
            sorted.append(hand)
    for i in range(len(sorted)):
        sum += (i+1) * int(sorted[i][1])
    print(sum)

def gettype_withjrule(hand):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for char in hand:
        if char == "2":
            count[0] += 1
        elif char == "3":
            count[1] += 1
        elif char == "4":
            count[2] += 1
        elif char == "5":
            count[3] += 1
        elif char == "6":
            count[4] += 1
        elif char == "7":
            count[5] += 1
        elif char == "8":
            count[6] += 1
        elif char == "9":
            count[7] += 1
        elif char == "T":
            count[8] += 1
        elif char == "J":
            count[9] += 1
        elif char == "Q":
            count[10] += 1
        elif char == "K":
            count[11] += 1
        elif char == "A":
            count[12] += 1
    pairs = 0
    trios = 0
    for n in count:
        if n == 2:
            pairs += 1
        elif n == 3:
            trios += 1
        elif n == 4:
            if count[9] >= 1:
                return 6
            return 5
        elif n == 5:
            return 6
    if (trios == 1) and (pairs == 1):
        if count[9] >= 1:
            return 6
        return 4
    elif trios == 1:
        if count[9] == 3:
            return 5
        elif count[9] == 1:
            return 5
        return 3
    elif pairs == 2:
        if count[9] == 2:
            return 5
        elif count[9] == 1:
            return 4
        return 2
    elif pairs == 1:
        if count[9] == 2:
            return 3
        elif count[9] == 1:
            return 3
        return 1
    elif count[9] == 1:
        return 1
    return 0

def keyfunc_withjrule(val):
    res = 0
    for i in range(5):
        x = 0
        try:
            x = int(val[0][i])
        except:
            if (val[0][i] == "T"):
                x = 10
            elif (val[0][i] == "J"):
                x = 0
            elif (val[0][i] == "Q"):
                x = 12
            elif (val[0][i] == "K"):
                x = 13
            elif (val[0][i] == "A"):
                x = 14
        res += 100**(5-i)*x
    return res

def task2():
    sum = 0
    input = getformatedinput()
    types = [[], [], [], [], [], [], []]
    for hand in input:
        hand[2] = gettype_withjrule(str(hand[0]))
        types[hand[2]].append(hand)
    sorted = []
    for type in types:
        type.sort(key = keyfunc_withjrule)
        for hand in type:
            sorted.append(hand)
    for i in range(len(sorted)):
        sum += (i+1) * int(sorted[i][1])
    print(sum)
    file = open("day7//output.txt", "w")
    file.write("")
    file.close()
    f = open("day7//output.txt", "a")
    for line in sorted:
        f.write(str(line))
    f.close()

task1()
task2()