# Find the divisors of a number
# Time complexity = Θ(n^(1/2)))
# Space complexity = Θ(1)


def printDivisor(n):
    i = 1
    while(i*i <=n):
        if (n%i == 0):
            print(i)
            if(i!= n/i):
                print(n/i)
        i = i+1

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(printDivisor(n))
