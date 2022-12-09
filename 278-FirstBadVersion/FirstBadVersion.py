# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(_self, _n):
        """
        :type n: int
        :rtype: int
        """
        lowerRange = 0
        upperRange = _n
        while not isBadVersion(lowerRange + 1):
            if isBadVersion((upperRange + lowerRange) / 2):
                upperRange = (upperRange + lowerRange) / 2
            else:
                lowerRange = (upperRange + lowerRange) / 2
        return lowerRange + 1
