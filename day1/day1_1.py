import sys

def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines

possible_chars = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
possible_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
lines = readInput("input_1_2.txt")

for line in lines:
    num1 = str(0)
    num2 = str(0)
    stop = 0
    for i in range(len(line)+1):
        for j in range(9):
            if possible_digits[j] in line[:i]:
                if (stop == 0):
                    num1 = str(j+1)
                    stop = 1
                break
        for char in line[:i]:
            if (char in possible_chars):
                if (stop == 0):
                    num1 = char
                    stop = 1
                break
        if (stop == 1):
            break
    
    stop = 0
    for i in range(len(line)+1):
        # print(line[::-1][:i][::-1])
        for j in range(9):
            if possible_digits[j] in line[::-1][:i][::-1]:
                if (stop == 0):
                    num2 = str(j+1)
                    stop = 1
                break
        if (stop == 1):
            break
        for char in line[::-1][:i][::-1]:
            if (char in possible_chars):
                if (stop == 0):
                    num2 = char
                    stop = 1
                break
        if (stop == 1):
            break
    if (int(num1) == 0):
        print("ACHTUNG")
        print(line)
        print("Number 1: " + num1 + " Number 2: " + num2)
    if (int(num2) == 0):
        print("ACHTUNG")
        print(line)
        print("Number 1: " + num1 + " Number 2: " + num2)
    sum += int(num1+num2)
    # print(line)
    # print("Number 1: " + num1 + " Number 2: " + num2)
print(sum)

# 54482 falsch

# 53015 falsch

# :cry:
# Luke hat 54489

# 54504 ist Richtig JUHUU