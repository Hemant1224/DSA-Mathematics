# find the palindrome number

def digitCount(n):
    res =  0
    while(n>0):
        n = n//10
        res = res + 1
    return res


def isPalindrome(n):
    temp = n
    rev = 0
    if digitCount(n) < 2:
        return "Please enter 2 or more than 2 digit"
        
    while(temp !=0):
        ld = temp % 10 # Mod gives the last value
        rev = rev * 10 + ld
        temp  = temp //10
    return rev == n

if __name__ == "__main__":
    num = int(input("Enter a number to check its palindrome or not: "))
    print(isPalindrome(num))
