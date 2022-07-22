def fib(n):
    # Define two variables and assign them the starting values of Fibonacci series which are 0,1
    a = 0
    b = 1

    # Edge cases in which the requested index is 0 or 1
    if n == 0:
        return a
    if n == 1:
        return b

    # Iterate in the range from 2 to the end of the end of the Fibonacci sequence
    for _ in range(2, n + 1):
        # Calculate the sum of a + b
        value = a + b

        # Set a equal to b
        a = b
        # Set b equal to value
        b = value
    # Return last calculated value
    return value


print(fib(10))
# 55
