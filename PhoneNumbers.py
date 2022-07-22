# Hash map of digits to letters list
lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

# List of valid words
validWords = ['dog', 'fish', 'cat', 'fog']


def makeWords_helper(digits, letters):
    # If there are not digits left we know we have reached the end of the word
    # This is the break point of the recursion
    if not digits:
        # Join the letters together into a word
        word = ''.join(letters)
        # Check if the word exists in validWords
        if word in validWords:
            # If do return the word inside a list
            return [word]
        # If not return empty list
        return []

    # Define a result list that will contain only the valid words that can be built with the received digits
    results = []
    # Obtain the letter characters from the digits
    chars = lettersMaps[digits[0]]
    # Iterate through the letter characters
    for char in chars:
        # Call this function in recursion and pass it all all the digits except the first one,
        # and the letters with current character appended
        # In this way we will check all possible letters combination,
        # for each combination we will reach a situation in which the are no more digits
        # in this situation we will check the if the letters combination is a valid word
        # if it does the valid word will be appended to the results list
        # if it doesn't empty list will be appended to the results meaning nothing will be appended
        # If you don't get it try do debug it :)
        results += makeWords_helper(digits[1:], letters + [char])
    return results


def makeWords(phone):
    # Create array of digits from the phone string
    digits = []
    for digit in phone:
        digits.append(int(digit))
    # Pass the array of digits to makeWords_helper and return it's return value
    return makeWords_helper(digits, [])


print(makeWords('364'))
