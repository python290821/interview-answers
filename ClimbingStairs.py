# Recursive solution
def staircase(n):
    # If number os stairs is less ot equal to 1 return 1, this is our step term of the recursion
    if n <= 1:
        return 1
    # Call this function recursively for n-1 and n-2,
    # this will be called until n<=1 and then go back up adding all the sums together
    return staircase(n - 1) + staircase(n - 2)

# Iteration solution- preferred (uses less space)
def staircase2(n):
    # Declare prev prevprev and curr variables
    prev = 1
    prevprev = 1
    curr = 0

    # Run in range from 2 till n+1
    for i in range(2, n + 1):
        # Current value is equal to prev value + prevprev value
        curr = prev + prevprev

        # Set prevprev to the current prev
        prevprev = prev
        # Set prev to current
        prev = curr
    # Return current after the iteration has finished
    return curr


print(staircase(5))
# 8

print(staircase2(5))
# 8
