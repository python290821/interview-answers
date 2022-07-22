def nqueens_helper(n, row, col, asc_diag, desc_diag, queen_pos):
    if len(queen_pos) == n:
        return queen_pos

    # Set the current row to the length of the queen_pos,
    # at the beginning queen_pos is empty so we start from the first row and advance
    curr_row = len(queen_pos)
    # Run in range from 0 to n
    for curr_col in range(n):
        # Check if the we can place the queen in the current position
        # (if one of the arguments is false we will know that this position is attacked by another queen)
        if col[curr_col] and row[curr_row] and asc_diag[curr_row + curr_col] and desc_diag[curr_row - curr_col]:
            # Set the current column to false since we are placing a queen there
            col[curr_col] = False
            # Set the current row to false since we are placing a queen there
            row[curr_row] = False
            # Set the current asc diagonal to false since we are placing a queen there
            asc_diag[curr_row + curr_col] = False
            # Set the current desc diagonal to false since we are placing a queen there
            desc_diag[curr_row - curr_col] = False

            # Add the queen to the position of current row and current column
            queen_pos.append((curr_row, curr_col))
            # Call this function again in recursion to find the next queen position
            nqueens_helper(n, row, col, asc_diag, desc_diag, queen_pos)

            # If we have reached the maximum n queens return the queen_pos
            if len(queen_pos) == n:
                return queen_pos

            # backtrack
            # Will run in case we can't place a queen in this column we will remove the queen and set the values of this
            # specific row, column and diagonals to true
            col[curr_col] = True
            row[curr_row] = True
            asc_diag[curr_row + curr_col] = True
            desc_diag[curr_row - curr_col] = True
            queen_pos.pop()

    return queen_pos


def nqueens(n):
    # Set all the columns rows and diagonals to true
    # We are creating a list of rows, list of columns, list of asc diagonals and list of desc diagonals
    # all those lists are filled with true values
    col = [True] * n
    row = [True] * n
    # The diagonal is represented as asc or dsc diagonal
    asc_diag = [True] * (n * 2 - 1)
    desc_diag = [True] * (n * 2 - 1)
    # Call the helper method with all the arguments needed
    return nqueens_helper(n, col, row, asc_diag, desc_diag, [])


print(nqueens(5))
# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
