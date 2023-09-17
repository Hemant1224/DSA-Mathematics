# Count the digit with time complexity Θ(digit count)

n = int(input("enter a number: "))
res  = 0
while(n > 0):
    n = n//10
    res = res + 1
print("Count of digit is: ", res)


