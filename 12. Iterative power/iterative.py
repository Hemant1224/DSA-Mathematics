def power(x,n):
    res = 1
    while n > 0:
        if n % 2!= 0:
            res = res * x
        x = x*x
        n = n//2
    return res

if __name__ == "__main__":
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))
    print(power(x,n))
