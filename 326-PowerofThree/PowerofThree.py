class Solution(object):
    def isPowerOfThree(_self, _n):
        """
        :type n: int
        :rtype: bool
        n == 3^x
        """
        if _n < 1:
            return False
        elif _n == 1:
            return True
        import math
        return (3 ** round(math.log(_n) / math.log(3))) == _n
