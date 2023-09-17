# Find factorial using recursion
# Time complexity = Θ(n)
# Space complexity = Θ(1)


def factorial(n):
    res = 1
    for i in range(1,n+1):  
        res = res * i
    return res

if __name__ == "__main__":
    n = int(input("Enter a number to calculate its factorial: "))
    print(factorial(n))
