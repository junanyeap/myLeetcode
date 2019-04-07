# turn x and y into binary 0000
# and judge hammingDistance

def addZero(binary,num):
    i = 0 
    temp = ""
    for i in range(num) :
        temp = temp + "0"
    temp = temp + binary
    # print("t:",temp,num)
    return temp

def decToBinary(num):
    binaryResult = ""
    binaryResultReverse = ""
    temp = num
    while temp != 0 :
        if temp % 2 == 1 :
            binaryResult = binaryResult + "1"
            temp = temp / 2
            temp = int(temp)
        else :
            binaryResult = binaryResult + "0"
            temp = temp / 2
            temp = int(temp)
    # reverse the binary result
    binaryResult = binaryResult[::-1]
    # while binaryTemp % 10 != 0 :
    #     binaryResultReverse = binaryResultReverse + str(binaryTemp % 10)
    #     binaryTemp = binaryTemp / 10
    #     binaryTemp = int(binaryTemp)
    #     print(binaryTemp)
    return binaryResult

# binary hammingDistance
def hammingDistance():
    i = 0
    print("Hamming Distance Calc ")
    x = int(input(""))
    y = int(input(""))
    diffCount = 0
    if x > 2147483648 or y > 2147483648 :
       print("too large")
    else : 
        xHam = decToBinary(x)
        yHam = decToBinary(y)

    if len(xHam) < len(yHam) :
        xHam = addZero(xHam,len(yHam)-len(xHam))
    elif len(yHam) < len(xHam) :
        yHam = addZero(yHam,len(xHam)-len(yHam))
    # for i in range (len(yHam)):
    print(xHam)
    print(yHam)
    
# normal hammingDistance
# def hammingDistance():
#     x = list(map(str,input("")))
#     y = list(map(str,input("")))
#     diffCount = 0
#     i = 0
#     if range(len(x)) == range(len(y)):
#         for i in range(len(x)):
#             if x[i] != y[i]:
#                 diffCount = diffCount + 1
#         print(diffCount)
#     else :
#         print("not same lenght")

hammingDistance()