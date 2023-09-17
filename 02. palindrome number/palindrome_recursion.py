def isPalindrome(n, result):
    if n==0:
        return result
    result = (result * 10) + (n % 10)
    return isPalindrome(n//10, result)

n = int(input("Please enter a number to check its palindrome or not: "))
if n == isPalindrome(n,0):
    print(f"the number {n} is palindrome.")
else:
    print(f"the number {n} is not palindrome.")
    


    
    
    
