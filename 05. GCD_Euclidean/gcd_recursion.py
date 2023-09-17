# Find GCD / Euclidean Algorithm
# Time complexity = Θ(log min(a,b))
# Space complexity = Θ(n)

def gcd(a,b):
    if b ==0:
        return a
    return gcd(b, a%b)

if __name__=="__main__":
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(gcd(a,b))
