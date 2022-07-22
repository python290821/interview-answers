
# Format the range string
def makerange(low, high):
    return str(low) + '-' + str(high)


def findRanges(nums):
    # Check cases where list of nums is empty than return empty list
    if not nums:
        return []

    # Declare empty list of ranges and low and high variable that
    # will be initialized with the value of the first number in the list
    ranges = []
    low = nums[0]
    high = nums[0]

    # Run over all the numbers in the list
    for n in nums:
        # Check if the current number is higher than the high number + 1
        if high + 1 < n:
            # If it's smaller we will know that there is a jump in the numbers and
            # we will add new range with low and high values
            ranges.append(makerange(low, high))
            # Set the low index to the current number since we are starting new range
            low = n
        # In each iteration we will change the high index to the current number
        high = n
    # After we finish to iterate we add the last range
    ranges.append(makerange(low, high))
    return ranges


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0-2', '5-5', '7-11', '15-15']
