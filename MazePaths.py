def paths_through_maze(maze):
    # Build a clone matrix of the maze that is initialized with zeros
    paths = [[0] * len(maze[0]) for _ in range(len(maze))]
    # Set the first item in the matrix to one since there is one way to get there. it's the staring point
    paths[0][0] = 1
    # Run over the rows in the maze matrix
    for i, row in enumerate(maze):
        # Run over the item in each row
        for j, val in enumerate(row):
            # If the value of the item in the maze is 1 meaning blocking
            # or if we are at the starting point just continue
            if val == 1 or (i == 0 and j == 0):
                continue

            # Declare two temporary variables leftPaths and topPaths that are equal to zero
            leftPaths = 0
            topPaths = 0

            # If we are not on the first row
            if i > 0:
                # Set the leftPaths to the same value as the item that on top of this value
                leftPaths = paths[i - 1][j]
            # If we are not on the first item of a row
            if j > 0:
                # Set the topPaths to the same value as the item that on left of this value
                topPaths = paths[i][j - 1]
            # Set the value of the current item to the sum of leftPaths and topPaths
            paths[i][j] = leftPaths + topPaths
    print(paths)
    # Extract the last item of the last row and return it. This is the result.
    return paths[-1][-1]


print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
