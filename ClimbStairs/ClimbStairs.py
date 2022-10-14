class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        tempCount = 0
        oneCount = 1
        twoCount = 0
        while n > 1:
            tempCount = oneCount
            oneCount = oneCount + twoCount
            twoCount = tempCount
            n -= 1
        return oneCount + twoCount
