# turn x and y into binary 0000
# and judge hammingDistance
def decToBinary(x):
    result = ""
    temp = x
    while temp != 0 :
        if temp%2 == 0 :
            result = result + "0"
            temp = temp / 2
        else :
            result = result + "1"
            temp = temp / 2
    return result

# binary hammingDistance
def hammingDistance():
    x = int(input(""))
    y = int(input(""))
    diffCount = 0
    print(decToBinary(x))

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