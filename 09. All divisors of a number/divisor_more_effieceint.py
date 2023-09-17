# Find the divisors of a number
# Time complexity = Θ(√n)
# Space complexity = Θ(1)

def printDivisor(n):
    i = 1
    while(i*i <= n):
        if (n%i==0):
            print(i)
        i = i + 1
    while(i >=1):
        if (n%i == 0):
            print(n/i)
        i = i-1


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(printDivisor(n))
