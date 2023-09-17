# Count the digit using recursion
# time complexity Θ(digit count)
# Aux space complexity Θ(digit count)

def countDigit(n):
    if n == 0:
        return 1
    return 1 + countDigit(n//10)

n = int(input("enter a number: "))
print(countDigit(n))
