class Solution(object):
    def num_islands(self, grid):
        # Edge case if the grid is empty return 0
        if not grid or not grid[0]:
            return 0
        # Extract number of rows and columns from the grid
        numRows, numCols = len(grid), len(grid[0])
        count = 0

        # Iterate through all the rows
        for row in range(numRows):
            # Iterate through each column in each row
            for col in range(numCols):
                # Check if the square is land
                if self._is_land(grid, row, col):
                    # Increase the count of islands by 1
                    count += 1
                    # Sink the land in the current square and all it's neighbor lands.
                    self._sinkLand(grid, row, col)
        return count

    def _sinkLand(self, grid, row, col):
        # First of all make sure that the square is land before sinking it
        if not self._is_land(grid, row, col):
            return
        # Change the square to water on the grid
        grid[row][col] = 0
        # Call this recursive method again for each ome of the 4 neighbor squares
        # in order to check if they are land and sink them.
        # If one of the neighbor square is land, this square will also call the recursive method for his neighbors
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self._sinkLand(grid, row + d[0], col + d[1])

    def _is_land(self, grid, row, col):
        # Edge cases when the square isn't on the grid
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
        # Return true if the square is land, false if it's water
        return grid[row][col] == 1


# 1 is for land 0 for water
grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]

print(Solution().num_islands(grid))
# 3
