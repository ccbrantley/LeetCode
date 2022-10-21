class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        myString = str(x)
        for index in range(len(myString)):
            if (myString[index] != myString[- index - 1]):
                return False
        return True
