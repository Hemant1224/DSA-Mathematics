# Find factorial using recursion
# Time complexity = Θ(n)
# Space complexity = Θ(n)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(fact(n))
