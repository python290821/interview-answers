def lengthOfLongestSubstring(str):
    # Declare variables
    # letter_pos is an empty dictionary in the beginning that will later hold the letters and their last position
    letter_pos = {}
    # Start index will be -1 at the beginning
    start = -1
    # End index will be -1 at the beginning
    end = 0
    # Max length of a string that we encountered
    max_length = 0

    # While we didn't reached the end of the string
    while end < len(str):
        # Extract the character in the current end index
        c = str[end]
        # Check if the character is already in the letter position dictionary
        if c in letter_pos:
            # Set the start index to the maximum between the previous start index
            # and the letter position of the extracted character
            start = max(start, letter_pos[c])

        # Set the max length as the maximum between previous max_length, and the current length of the unique characters
        max_length = max(max_length, end - start)

        # Set the position of the character in the dictionary to the current end position
        letter_pos[c] = end
        # Add 1 to the end value
        end += 1
    return max_length


print(lengthOfLongestSubstring('aabcbbeacc'))
