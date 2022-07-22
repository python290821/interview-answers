from collections import defaultdict


def find_palindrome(str):
    # Define a default dictionary of characters,
    # the dictionary is empty in the beginning but each key that is added to the dictionary gets the value 0
    char_counts = defaultdict(int)

    # Run over all the characters in the string
    for c in str:
        # Add 1 to the value of the character in the dictionary
        # If the character doesn't exist, it adds new character with value 0 and than add 1 to it
        # If the character exist it's just adding 1 to the value
        char_counts[c] += 1

    # Define empty string for the palindrome and the odd character
    pal = ''
    odd_char = ''

    # Run over all the characters and their values in the dictionary
    for c, cnt in char_counts.items():
        # If the value of the character is even
        if cnt % 2 == 0:
            # Add to the palindrome the character as much times as the value/2.
            # If the value is 2 than we add 1 character if it's 4 we add two characters
            pal += c * (cnt // 2)
        # Else if, the value of the character is uneven, and the value of odd_char is empty string
        elif odd_char == '':
            # Set the odd char to the current
            odd_char = c
            # Add to the palindrome the character as much times as the value/2.
            # If the value is 1 than we add zero characters if it's 3 we add one character
            pal += c * (cnt // 2)
        # Else if, the value of the character is uneven, and the value of odd_char is not an empty string
        else:
            # Return false because we can't create a palindrome when more than one character has uneven count
            return False
        # Return the palindrome string + odd character + palindrome string in reverse
    return pal + odd_char + pal[::-1]


print(find_palindrome('foxfo'))
# foxof
