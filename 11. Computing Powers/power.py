def power(x,n):
    res = 1
    for i in range(n):
        res = res * x
    return res


if __name__ == "__main__":
    x = int(input("Enter a number: "))
    n = int(input("Enter a number: "))
    print(power(x,n))
