def romanToInt(x):
    num_lst = []
    # define roman num
    h = {'I' :1, 'V': 5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
    i = 0
    while i <= len(x)-1:
        if i == 0:
            num_lst.append(h[x[i]])
            i += 1
        elif h[x[i]] > h[x[i-1]]:
            num_lst.append( h[x[i]]-h[x[i-1]])
            num_lst.remove(h[x[i-1]])
            i += 1
        else:
            num_lst.append(h[x[i]])
            i += 1
    return sum(num_lst)

print(romanToInt(input()))