def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # recursion call


print(factorial(5))  # must be 120
