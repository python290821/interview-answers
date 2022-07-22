class Solution:
    def romanToInt(self, s):
        # Create Dictionary data structure of [str, int] that we hold the definition of the roman numeric values
        romanNumerals = {'I': 1, 'V': 5, 'X': 10,
                         'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Define variables
        prev = 0
        sum = 0
        # Iterate through the string backwards
        for i in s[::-1]:
            curr = romanNumerals[i]  # Define a variable that will represent the current character
            if prev > curr:  # If prev is larger than the current we will subtract
                sum -= curr
            else:  # Else, we will add it
                sum += curr
            # Another option to write the if else statement in one line
            # sum = sum + (-curr if prev > curr else curr)

            prev = curr  # Set prev value to be equal to the curr value
        return sum


n = 'MCMIV'
print(Solution().romanToInt(n))
# 1904
