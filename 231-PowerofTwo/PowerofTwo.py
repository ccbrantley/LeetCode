class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = 0
        while 2 ** power < n:
            power += 1
        return 2 ** power == n
