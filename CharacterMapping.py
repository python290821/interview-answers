def has_character_map(s1, s2):
    # Check if the length of the two strings is different
    if len(s1) != len(s2):
        return False

    # Define a dictionary of characters
    chars = {}
    # Run over the range from 1 to the length of the strings
    for i in range(len(s1)):
        # If the character in the first string is not in the dictionary
        if s1[i] not in chars:
            # Add it to the dictionary together with the corresponding character from the second string
            chars[s1[i]] = s2[i]
        # Else, If the character in the first string is in the dictionary
        else:
            # Check that the matching character in the second string is not the same as in the dictionary.
            # If so return false
            if chars[s1[i]] != s2[i]:
                return False
    # If we finished the for loop we return true since all the characters have been mapped
    return True


print(has_character_map('abc', 'def'))
# True

print(has_character_map('aac', 'def'))
# False
