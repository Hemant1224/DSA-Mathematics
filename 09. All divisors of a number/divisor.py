# Find the divisors of a number
# Time complexity = Θ(n)
# Space complexity = Θ(1)

def printDivisor(n):
    for i in range(1, n+1):
        if(n%i==0):
            print(i)
        
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(printDivisor(n))
