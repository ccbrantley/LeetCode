class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        tempX = x
        if tempX > 0:
            oddNumber = 1
            oddCount = 0
            while tempX > 0:
                oddNumber += 2
                oddCount += 1
                tempX -= oddNumber
            return oddCount
        return 0
