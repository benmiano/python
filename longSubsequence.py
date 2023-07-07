# Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

# store array
# return array of increasing subsequence
# create variable array of longest increasing subsequence
# loop through array, compare array of 1st n 2nd no ++, set subsequence to longer array
class SubSequence:
    def __init__(self, arrayInput: list) -> None:
        self.arrayInput = arrayInput
        self.subsequence = []

    def compareSubsequences(self, array2: list):
        if len(self.subsequence) < len(array2):
            self.subsequence = array2

    # def setSubsequence(self):
        position = 0
        localArray = []
        while position < (self.arrayLength):
            if (len(localArray))== 0:
                localArray.append(self.arrayInput[0])
            if self.arrayInput[position]>self.arrayInput[position+1]:
                position+=1
                continue
            if self.arrayInput[position]< self.arrayInput[position+1]:
                localArray.append(self.arrayInput[position+1])
                position+=1
            else:
                continue
            # if self.arrayInput[0] > self.arrayInput[1]:
            #     return False
        return localArray

    def addToSubsequence(self, j):
        position = j
        localArray=[]
        while position < len(self.arrayInput):
            localArray.append(self.arrayInput[position])
            position = self.arrayInput.index(self.arrayInput[position])
            if(self.arrayInput[position]>self.arrayInput[position+1]):
                position += 1
                continue
        return localArray
    
    # loop through array
    def getLongestSubsequence(self):
        for i in range(len(self.arrayInput)):
            self.compareSubsequences(self.addToSubsequence(i))

mylongestSubsequence = SubSequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
mylongestSubsequence.getLongestSubsequence()
print (mylongestSubsequence.subsequence())