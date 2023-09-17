# Naive Approach

def countZeros(n):
    fact =1 
    for i in range(2, n+1):
        fact =  fact * i
    res = 0
    while(fact % 10 == 0):
        res = res + 1
        fact  =  fact //10
    return res

if __name__=='__main__':
    n = int(input("Enter a number :"))
    print(countZeros(n))



