# Time complexity = Θ(log min(a,b))

def gcd(a,b):
    while(a!=b):
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

if __name__ =="__main__":
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(lcm(a,b))


