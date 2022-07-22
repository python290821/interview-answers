# Use a class to show oop skills
class Grid(object):
    # This class will have one variable and it's the matrix
    def __init__(self, matrix):
        self.matrix = matrix

    # A private function that will check a word from left to right
    def __wordSearchRight(self, index, word):
        # Run over the range between 0 and the length of the columns of the the matrix
        for i in range(len(self.matrix[index])):
            # Check if the character in current index in the word is not the same
            # as the character in current index in the matrix
            if word[i] != self.matrix[index][i]:
                return False
        return True

    # A private function that will check a word from top to bottom
    def __wordSearchBottom(self, index, word):
        # Run over the range between 0 and the length of the rows of the the matrix
        for i in range(len(self.matrix)):
            # Check if the character in current index in the word is not the same
            # as the character in current index in the mat
            if word[i] != self.matrix[i][index]:
                return False
        return True

    # A public function that will search for a word
    def wordSearch(self, word):
        # Run over the range between 0 and the length of the rows of the the matrix
        for i in range(len(self.matrix)):
            # Invoke __wordSearchRight method and check what it returns
            if self.__wordSearchRight(i, word):
                return True
        # Run over the range between 0 and the length of the columns of the matrix
        for i in range(len(self.matrix[0])):
            # Invoke __wordSearchBottom method and check what it returns
            if self.__wordSearchBottom(i, word):
                return True
        return False


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

print(Grid(matrix).wordSearch('FOAM'))
# True
