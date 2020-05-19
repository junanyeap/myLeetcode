def twoSum(arr,target):
    dict = {}
    result = [-1,-1]
    for i in range(len(arr)):
        dict[arr[i]] = i

    for i in range(len(arr)):
        comp = target - arr[i]
        if comp in dict and i!= dict[comp] :
            result[0] = i
            result[1] = dict[comp]

    return result


def main():
    myArr = [2,7,11,15]
    target = 9
    result = twoSum(myArr,target)
    print(result)

main()