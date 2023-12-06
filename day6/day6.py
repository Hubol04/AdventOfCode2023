def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines

def getformatedinput():
    lines = readInput("day6//input.txt")
    lines.append("")
    formated = []
    tmp1 = lines[0].split(":",1)[1].split()
    tmp2 = lines[1].split(":",1)[1].split()
    formated.append(tmp1)
    formated.append(tmp2)    
    return formated

#Formula: a=time hold button      (racetime-a)*(a)  for example: racetime = 7 --> 7*a - a^2 --> 1st Derivation: -2*a+7 = 0 --> 3.5 is max
#                                                                                                               a = 7/2
def getalternatives(racetime, record):
    maxhold = racetime/2
    possibilities = 0
    if (int(maxhold) == int(maxhold+0.5)):
        possibilities = -1
    maxhold = int(maxhold)
    for i in range(maxhold+1):
        if ((racetime - i) * i > record):
            possibilities += 2
    return possibilities
    


def task1():
    input = getformatedinput()
    product = 1
    for i in range(len(input[0])):
        product *= getalternatives(int(input[0][i]), int(input[1][i]))
    print(product)

def getformatedinput2():
    lines = readInput("day6//input.txt")
    lines.append("")
    formated = []
    tmp1 = lines[0].split(":",1)[1].replace(" ", "")
    tmp2 = lines[1].split(":",1)[1].replace(" ", "")
    formated.append(tmp1)
    formated.append(tmp2)    
    return formated

def task2():
    input = getformatedinput2()
    print(getalternatives(int(input[0]), int(input[1])))


task1()
task2()