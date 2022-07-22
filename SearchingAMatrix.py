def searchMatrix(mat, value):
    # Define edge case in which the matrix is empty
    if len(mat) == 0:
        return False

    # Get the dimensions of the matrix into two variables: rows and cols
    rows = len(mat)
    cols = len(mat[0])

    # Set low and high variables, low will be equal to 0, high will be equal to the result of rows multiplied with cols
    # In other words the high will be last element index
    low = 0
    high = rows * cols

    # Run while the low value is smaller than the high value
    while low < high:
        # Calculate the middle index
        mid = (low + high) // 2
        # Extract the value from the matrix, first index is of the row, second index is of the item
        mid_value = mat[mid // cols][mid % cols]

        # If the mid_value we extracted from the matrix is the same as the searched value return true
        if mid_value == value:
            return True
        # If the mid_value we extracted from the matrix is smaller than the value set the low index to the mid index +1
        if mid_value < value:
            low = mid + 1
        # Else (mid_value is larger than the value), set the high index as the mid
        else:
            high = mid

    # If we finished running the loop
    # it means no number was found that is the same as the searched number so return false
    return False


# The matrix is built from rows and items
mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
