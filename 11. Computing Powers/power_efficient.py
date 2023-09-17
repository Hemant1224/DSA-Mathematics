def power(x,n):
    if n == 0:
        return 1
    temp = power(x,n//2)
    temp = temp * temp
    if n % 2 == 0:
        return temp
    else:
        return temp * x

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    n = int(input("Enter a number: "))
    print(power(x,n))
