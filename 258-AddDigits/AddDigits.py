class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sb = str(num)
        while len(sb) > 1:
            total = 0
            for x in sb:
                total += int(x)
            sb = str(total)
        return int(sb)
