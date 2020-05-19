def isPalindrome(x):
    if(x < 0 or (x % 10 == 0 and x != 0)):
        return False
    else:
        val = 0
        while(x > val):
            val = val * 10 + x % 10
            x = x // 10

        return val == x or x == (val // 10)

result = isPalindrome(int(input()))
print(result)