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
    minred = 0
    mingreen = 0
    minblue = 0
    for val in values:
        if (val[0] > minred):
            minred = val[0]
        if (val[1] > mingreen):
            mingreen = val[1]
        if (val[2] > minblue):
            minblue = val[2]
    # print("red: " + str(minred)+ " green: " + str(mingreen) + " blue: " + str(minblue))
    sum += minred*mingreen*minblue
    # print("Zeile passt: " + str(i+1))
print(sum)