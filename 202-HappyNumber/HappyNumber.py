class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = set()
        while True:
            digits.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
            if n == 1:
                return True
            if n in digits:
                return False
