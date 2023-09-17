# efficient approach 

def isPrime(n):
    if n == 1:
        return False
    i = 2
    while(i*i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

if __name__  == "__main__":
    a = int(input("Enter number to check its prime or not: "))
    print(isPrime(a))
