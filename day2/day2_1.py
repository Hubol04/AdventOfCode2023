def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines

def formatinput(input):
    formated = []
    line = input.split(":", 1)[1].split(";")
    for s in line:
        red = 0
        green = 0
        blue = 0
        tmp = s.split(",")
        for val in tmp:
            x = val.split()
            if ("red" in x[1]):
                red = int(x[0])
            if ("green" in x[1]):
                green = int(x[0])
            if ("blue" in x[1]):
                blue = int(x[0])
        formated.append([red, green, blue])
    return formated

#main
lines = readInput("day2//input.txt")
sum = 0
for i in range(len(lines)):
    values = formatinput(lines[i])
    # print("formated:" + str(values))
    toobig = 0
    for val in values:
        if (val[0] > 12):
            toobig = 1
            break
        if (val[1] > 13):
            toobig = 1
            break
        if (val[2] > 14):
            toobig = 1
            break
    if (toobig == 0):
        sum += i+1
        # print("Zeile passt: " + str(i+1))
print(sum)