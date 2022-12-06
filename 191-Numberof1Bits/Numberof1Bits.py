class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([int(x, 2) for x in bin(n)[2::]])
