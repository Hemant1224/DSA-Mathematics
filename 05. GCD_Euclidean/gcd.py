# Find GCD 
# Time complexity = Θ(log min(a,b))
# Space complexity = Θ(1)


def gcd(a,b):
    while(a!=b):
        if a > b:
            a = a - b
        else: 
            b = b - a
    return f"The GCD of both the number is {a}"

if __name__ =='__main__':
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(gcd(a,b))
