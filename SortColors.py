from collections import defaultdict


class Solution(object):
    # Solution using hash maps
    def sortColors(self, colors):
        # defaultdict evaluates all the values to 0 and will used as our hashmap
        colorsMap = defaultdict(int)
        # Iterate through each color and increase the counter of the current color by 1
        for c in colors:
            colorsMap[c] += 1

        # Index that will help us track the where to set the new color
        index = 0

        # For each color we will:
        # Generate range from 0 to the counter of the color and run over it
        # For example if we encountered 3 black colors we will run 3 times
        # Than in each iteration of a specific color we will set the color in the current index
        # and increase the index by 1
        for i in range(colorsMap[0]):
            colors[index] = 0
            index += 1
        for i in range(colorsMap[1]):
            colors[index] = 1
            index += 1
        for i in range(colorsMap[2]):
            colors[index] = 2
            index += 1

    # Solution using indices
    def sortColor2(self, colors):
        # Declare low, high and current index variables
        lowIndex = 0  # First and lowest index
        highIndex = len(colors) - 1  # Last and highest index
        currIndex = 0  # Current index is 0 at the beginning

        # Run while the current index is less or equal to the high index
        while currIndex <= highIndex:
            # If the color in the current index is equal to 0 (blue for example)
            if colors[currIndex] == 0:
                # Swap the color in the low index and color in the current index
                colors[lowIndex], colors[currIndex] = colors[currIndex], colors[lowIndex]
                lowIndex += 1
                currIndex += 1
            # Else, if the color in the current index is equal to 2 (black for example)
            elif colors[currIndex] == 2:
                # Swap the color in the high index and color in the current index
                colors[highIndex], colors[currIndex] = colors[currIndex], colors[highIndex]
                highIndex -= 1
            # Else, if the color in the current index is equal to 1 (red for example)
            else:
                currIndex += 1


colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColors(colors)
print(colors)
# [0, 0, 1, 1, 1, 2, 2]

colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColor2(colors)
print(colors)
# [0, 0, 1, 1, 1, 2, 2]
