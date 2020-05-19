def longestCommonPrefix(x):
    result = ""
    compTemp = ""
    if(x is not None and len(x) != 0):
        result = str(x[0]);
        for i in range(1,len(x)):
            temp = x[i]
            for j in range(min(len(result),len(temp))):
                if(result[0] != temp[0]):
                    return ""
                if(result[j] == temp[j]):
                    compTemp = compTemp + temp[j] 
            result = compTemp
            compTemp = ''
    return result

input = ["flower","flow","flight"]
print(longestCommonPrefix(input))