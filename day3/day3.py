def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines

def getformatedinput():
    lines = readInput("day3//input.txt")
    formated = []
    for line in lines:
        tmp = []
        for char in line:
            tmp.append(char)
        formated.append(tmp)
    return formated

def checksymbols(whitelist, blacklist, input, i, j): #gives value 0 (not valid) or 1 (valid)
    for a in range(3):
        for b in range(3):
            if (i+b-1 >= 0) and (i+b-1 < len(input)) and (j+a-1 >= 0) and (j+a-1 < len(input[i+b-1])) and (input[i+b-1][j+a-1] not in blacklist) and ((len(whitelist) == 0) or (input[i+b-1][j+a-1] in whitelist)):
                if (b-1 != 0) or (a-1 != 0):
                    return 1 #valid
    return 0 #not valid

###
# gives back a string of length 9
# example 011100111 means
# 0 1 1  -   1 2 3
# 1 0 0  -   4 5 6
# 1 1 1  -   7 8 9
# at position 2,3,4,7,8,9 is a symbol from the whitelist/ not from the blacklist
###
def checksymbols_binary(whitelist, blacklist, input, i, j): 
    res = ""
    for b in range(3):
        for a in range(3):
            if (i+b-1 >= 0) and (i+b-1 < len(input)) and (j+a-1 >= 0) and (j+a-1 < len(input[i+b-1])) and (input[i+b-1][j+a-1] not in blacklist) and ((len(whitelist) == 0) or (input[i+b-1][j+a-1] in whitelist)):
                if (b-1 != 0) or (a-1 != 0):
                    res += "1" #valid
                else:
                    res += "0" #symbol at position 5 is not of interest because its the symbol we search around --> not valid
            else:
                res += "0" #not valid
    return res

def task1():
    sum = 0
    whitelist = []
    filter = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    input = getformatedinput()
    k = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if k>0:
                k = k-1
            else:
                number = ""
                valid = 0
                while ((j+k < len(input[i])) and (input[i][j+k] in num)):
                    if (checksymbols(whitelist, filter, input, i, j+k) == 1):
                        valid = 1
                    number += input[i][j+k]
                    k += 1
                if (valid == 1):
                    sum += int(number)
    print(sum)

def getnumber(input, i, j):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    number = input[i][j]
    k = 1
    while (j+k<len(input[i]) and (input[i][j+k] in num)):
        number = number + input[i][j+k]
        k += 1
    k = 1
    while ((j-k>=0) and (input[i][j-k] in num)):
        number = input[i][j-k] + number
        k += 1
    return number

def task2():
    input = getformatedinput()
    sum = 0
    whitelist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    blacklist = ['.']
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "*":
                tmp = checksymbols_binary(whitelist, blacklist, input, i, j)
                if (int(tmp) > 0):
                    num = [0,0]
                    count = 0
                    for k in range(0, len(tmp), 3):
                        tmp2 = tmp[k:k+3]
                        if (tmp2 == "101"):
                            count += 2
                            if (count>2):
                                break
                            num[0] = int(getnumber(input, int(i+k/3-1), j-1))
                            num[1] = int(getnumber(input, int(i+k/3-1), j+1))
                        elif (tmp2[0] == "1"):  #100, 110, 111
                            count += 1
                            if (count>2):
                                break
                            num[count-1] = int(getnumber(input, int(i+k/3-1), j-1))
                        elif (tmp2[1] == "1"):   #010, 011
                            count += 1
                            if (count>2):
                                break
                            num[count-1] = int(getnumber(input, int(i+k/3-1), j))
                        elif (tmp2[2] == "1"):   #001
                            count += 1
                            if (count>2):
                                break
                            num[count-1] = int(getnumber(input, int(i+k/3-1), j+1))
                    if count == 2:
                        sum += num[0] * num[1]
    print(sum)
                            
print("Task 1:")
task1()

print("Task 2:")
task2()
