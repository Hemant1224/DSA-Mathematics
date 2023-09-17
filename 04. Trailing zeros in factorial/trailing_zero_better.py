def countZeros(n):
    res = 0
    i = 5
    while(i<=5):
        res = res + n//i
        i = i * 5
    return res

if __name__== "__main__":
    n = int(input("Enter a number: "))
    print(countZeros(n))
