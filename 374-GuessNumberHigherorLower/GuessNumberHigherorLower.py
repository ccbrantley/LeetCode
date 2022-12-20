# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lowGuess = 1
        highGuess = n
        myGuess = highGuess / 2
        while guess(myGuess) != 0:
            # too high.
            if guess(myGuess) == -1:
                highGuess = myGuess - 1
            # too low.
            else:
                lowGuess = myGuess + 1
            myGuess = (highGuess + lowGuess) / 2
        return myGuess
