class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segCount = 0
        for x in s.split(" "):
            if x != "":
                segCount += 1
        return segCount
