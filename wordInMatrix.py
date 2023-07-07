# Given a 2D matrix of characters and a target word, 
# write a function that returns whether the word can be found in the matrix by going 
# left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

class WordMatrix:
    def __init__(self, matrix:list) -> None:
        self.matrix = matrix

# check rows/horizontally
    def horizontally(self, wordInput):
        isWordPresent = wordInput + " is not present in any row"
        for x in self.matrix:
            word = ""
            for i in x:
                word = word + i
            if wordInput in word:
                isWordPresent = (wordInput + " is present in row number " + format(self.matrix.index(x)+1))
                break     
        print (isWordPresent)

# check columns/vertically
    def vertically(self, wordInput):
        isWordPresent = wordInput + " is not present in any column"
        count = 0
        while count < len(self.matrix[0]):
            word=""
            for x in self.matrix:
                word = word + (x[count])
            if wordInput in word:
                isWordPresent = wordInput + " is present in column number " + format(count+1)
                break
            count+=1
        print(isWordPresent)

    def checkWord(self, wordInput):
        self.horizontally(wordInput)
        self.vertically(wordInput)

wordMatrix = WordMatrix([['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']])

wordMatrix.checkWord("FOAM")

