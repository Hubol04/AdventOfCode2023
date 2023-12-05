import threading

def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines

def getformatedinput():
    lines = readInput("day5//input.txt")
    lines.append("")
    formated = []
    tmp = []
    for i in range(len(lines)):
        if (i == 0):
            tmp = lines[0].split(":",1)[1].split()
        else:
            if (":" in lines[i]):
                tmp = []
            elif (len(lines[i]) == 0):
                formated.append(tmp)
            else:
                tmp.append(lines[i].split())
    return formated

def task1():
    input = getformatedinput()
    vals = []
    for seed in input[0]:
        val = int(seed)
        for i in range(1, len(input)):
            for conversion in input[i]:
                tmp = int(val) - int(conversion[1])
                if (tmp < int(conversion[2])) and (tmp >= 0):
                    val = int(conversion[0]) + tmp
                    break
        vals.append(val)
    print(min(vals))

def task2():
    input = getformatedinput()
    vals = []
    for j in range(0, len(input[0]),2):
        for seed in range(int(input[0][j]), int(input[0][j]) + int(input[0][j+1])):
            val = int(seed)
            for i in range(1, len(input)):
                for conversion in input[i]:
                    tmp = int(val) - int(conversion[1])
                    if (tmp < int(conversion[2])) and (tmp >= 0):
                        val = int(conversion[0]) + tmp
                        break
            vals.append(val)
    print(min(vals))

def task2thread():
    threads = []
    input = getformatedinput()
    vals = []
    for j in range(0, len(input[0]),2):
        for seed in range(int(input[0][j]), int(input[0][j]) + int(input[0][j+1])):
            x = threading.Thread(target = threadwork, args = (seed, vals, input))
            threads.append(x)
            x.start()
    count = 0
    for thread in threads:
        thread.join()
        count += 1
        if count%100 == 0:
            print(count)
    print(min(vals))

def threadwork(seed, vals, input):
    val = int(seed)
    for i in range(1, len(input)):
        for conversion in input[i]:
            tmp = int(val) - int(conversion[1])
            if (tmp < int(conversion[2])) and (tmp >= 0):
                val = int(conversion[0]) + tmp
                break
    vals.append(val)

task1()
task2thread()