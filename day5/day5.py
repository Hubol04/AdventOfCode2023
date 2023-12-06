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

def task2brute():
    input = getformatedinput()
    min = 46200000   #already in previous run tested
    while (0==0):
        if(min%100000 == 0):
            print(min)
        val = min
        for i in range(len(input)-1, 0, -1):
            for conversion in input[i]:
                tmp = int(val) - int(conversion[0])
                if (tmp < int(conversion[2])) and (tmp >= 0):
                    val = int(conversion[1]) + tmp
                    break
        for k in range(0, len(input[0]), 2):
            if (val >= int(input[0][k])) and (val < int(input[0][k]) + int(input[0][k+1])):
                print("Min is: " + str(min))
                return
        min += 1

def brutethreads(min, stop, found, input):
    while (min < stop):
        if(min%100000 == 0):
                print(min)
        val = min
        for i in range(len(input)-1, 0, -1):
            for conversion in input[i]:
                tmp = int(val) - int(conversion[0])
                if (tmp < int(conversion[2])) and (tmp >= 0):
                    val = int(conversion[1]) + tmp
        for k in range(0, len(input[0]), 2):
            if val in range(int(input[0][k]), int(input[0][k]) + int(input[0][k+1])):
                print("Min is: " + str(min))
                found = 1
                return
        min += 1
    print("Values from: " + str(min) + " to: " + str(stop) + " no seed found")

def task2brutethreads():
    threads = []
    found = 0
    input = getformatedinput()
    min = 0
    while (0==0):
        for i in range(4):
            x = threading.Thread(target = brutethreads, args = (min+i*1000000, min+(i+1)*1000000, found, input))
            threads.append(x)
            x.start()
            print("Thread " + str(i) + " created.")
        for thread in threads:
            print("Wait for Thread " + str(i) + ".")
            thread.join
            threads = []
        if found == 1:
            print("Stop because found Min")
            return
        else:
            min += 4000000

task1()
task2brute()    #0 to 46.200.000 already tested